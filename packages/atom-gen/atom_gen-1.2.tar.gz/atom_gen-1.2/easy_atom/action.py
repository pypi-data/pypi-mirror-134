#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Frederic Laurent'
__version__ = "1.0"
__copyright__ = 'Copyright 2017, Frederic Laurent'
__license__ = "MIT"

import logging
import os.path
import shutil

from ftplib import FTP

import mailer
import requests
import tempfile
import tweepy, tweepy.errors

from easy_atom import helpers, content


class Action:
    """
    Abstract class
    Base des actions
    """

    def __init__(self, conf_filename=None, conf=None):
        """
        Constructeur initialisant l'action avec des données de configuration

        :param conf_filename: Fichier contenant les paramètres de configuration
        :param conf: Paramètres directement fournis dans 1 dictionnaire
        """
        self.conf = conf
        self.conf_filename = conf_filename
        self.logger = logging.getLogger('action')

        self.logger.debug("Fichier de configuration : %s" % self.conf_filename)
        if conf_filename:
            self.load_config()

    def load_config(self):
        """
        Lecture des données de configuration. Les donnees sont accessibles dans conf
        :return: -
        """
        if self.conf_filename and os.path.exists(self.conf_filename):
            self.logger.debug("Load configuration file = {}".format(self.conf_filename))
            self.conf = helpers.load_json(self.conf_filename)

    def process(self, infos):
        raise Exception("Abstract method")


class SendMailAction(Action):
    """
    Action : envoi de mail
    """

    def __init__(self, conf_filename=None, conf=None):
        Action.__init__(self, conf_filename=conf_filename, conf=conf)
        self.logger.debug("Mail configuration : %s" % self.conf)

    def process(self, infos):
        """
        En prenant les informations dans la configuration fournie, 
        un mail est envoyé en se basant sur les informations contenues dans le paramètre

            subject = infos['title']
            content = mise en forme avec make_xhtml

        :param infos: données à envoyer par mail
        :return: -
        """
        self.logger.debug("Send Mail notification, infos = {}".format(infos))
        if self.conf:
            for dest in self.conf['to']:
                message = mailer.Message(From=self.conf['from'], To=dest, charset="utf-8")
                message.Subject = infos['title']

                message.Html = content.xml2text(content.make_xhtml(root=None, entry=infos), 'utf-8')
                sender = mailer.Mailer(host=self.conf['server'], port=self.conf['port'],
                                    usr=self.conf['user'], pwd=self.conf['passwd'],
                                    use_ssl=self.conf['usessl'])
                sender.send(message)
                self.logger.debug("Mail sent to {}".format(dest))


class UploadAction(Action):
    """
    Action de téléchargement (upload) de fichiers sur un site FTP 
    Les données de connexion au serveur FTP sont fournies via les données de
    configuration
    Voir le constructeur.
    """

    def process(self, infos):
        """
        Télécharge tous les fichier sur le site FTP distant
        :param infos: Liste des fichiers à télécharger : type: List
        :return: -
        """

        with FTP(self.conf["server"], self.conf["user"], self.conf["passwd"]) as ftp_cnx:
            ftp_cnx.cwd(self.conf["remotedir"])
            for filename in infos:
                if os.path.exists(filename):
                    self.logger.debug("Upload file : %s -> %s" % (filename, os.path.basename(filename)))
                    fh = open(filename, 'rb')  # file to send
                    ftp_cnx.storbinary('STOR %s' % os.path.basename(filename), fh)  # send the file
                    fh.close()  # close file and FTP
                else:
                    self.logger.warn("File %s not found" % filename)


class DownloadAction(Action):
    """
    Action de téléchargement de fichiers définis par des URL
    Les fichiers sont téléchargés localement.
    """

    def download(self, url):
        """
        Télécharge tous les fichiers en local dans le repertoire défini dans les paramètres de 
        configuration avec la clé download_dir. Si aucun répertoire local n'est défini, un répertoire
        temporaire est créé.

        :param url: URL du fichier distant à télécharger
        :return: Chemin absolu du fichier téléchargé.
        """
        
        if not self.conf:
            self.conf = {}
        if 'download_dir' not in self.conf:
            self.conf['download_dir'] = tempfile.mkdtemp(suffix='action', prefix='easy_atom')

        return self.download_url(self.conf['download_dir'], url)

    @staticmethod
    def download_url(download_dir, url):
        if download_dir and not os.path.exists(download_dir):
            os.makedirs(download_dir)

        local_filename = os.path.join(download_dir, url.split('/')[-1])

        req = requests.get(url, stream=True)
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(req.raw, f)

        return os.path.abspath(local_filename)

    def process(self, infos):
        """
        Télécharge en local les fichiers désignés par des URL dans les données info.
        Les fichiers peuvent être désignés par la clé <url> ou par la clé <files>

        Exemple :
        infos = {'type': 'CCAM',
        'version': 49.0,
        'date': '2017-10-21T08:14:06.351015+00:00',
        'url': None,
        'files': [
        'https://www.ameli.fr/fileadmin/user_upload/documents/CCAM04900_DBF_PART1.zip',
        'https://www.ameli.fr/fileadmin/user_upload/documents/CCAM04900_DBF_PART2.zip',
        'https://www.ameli.fr/fileadmin/user_upload/documents/CCAM04900_DBF_PART3.zip']}

        :param infos: dictionnaire contenant les informations sur les données à télécharger
        :return: Liste des fichiers locaux telechargés, type: List
        """
        files = []

        if self.conf and self.conf['download']:
            self.logger.info("Téléchargement des fichiers...")
            if infos["url"]:
                fn = self.download(infos["url"])
                files.append(fn)
            if len(infos["files"]):
                for f in infos["files"]:
                    fn = self.download(f)
                    files.append(fn)

        return files

   
class TweetAction(Action):
    """
        Permet de tweeter un texte. Les paramètres du compte sont passés
        au constructeur.
    """
    def process(self, infos):
        """
            tweet les informations contenues dans infos

        :param infos: texte a tweeter
        :return: URL du tweet ou None si erreur
        """
        
        auth = tweepy.OAuthHandler(self.conf['consumer_key'], self.conf['consumer_secret'])
        auth.set_access_token(self.conf['access_token'], self.conf['access_token_secret']) 
        api = tweepy.API(auth)

        id_ret = None
        self.logger.info("Tweet : {}".format(infos))
        if isinstance(infos, str):
            try:
                ret = api.update_status(status=infos)
                self.logger.info("JSON = {}".format(ret._json))
                _url_parts=['https://www.twitter.com', 
                    ret._json['user']['screen_name'],
                    'status',
                    ret._json['id_str']]
                return '/'.join(_url_parts)

            except tweepy.errors.TweepyException as te:
                self.logger.warning("Erreur de tweet : {} ".format(te))
        
        return id_ret