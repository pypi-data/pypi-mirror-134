#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Fonctions de production de contenu


"""
__author__ = 'Frederic Laurent'
__version__ = "1.0"
__copyright__ = 'Copyright 2017, Frederic Laurent'
__license__ = "MIT"

import os.path
import lxml.etree
from lxml.etree import Element, SubElement
from easy_atom import helpers


def make_xhtml(root, entry):
    """
    Creation d'un contenu XHTML pour une entree ATOM
    content > div > article > blabla

    si files fait partie des informations dans l'entree, une section telechargement est inseree
    contenu : text

    :param root: noeud XML du père du contenu
    :param entry: données de l'entrée ATOM
    :return: noeud XML produit
    """
    content_elt = xmlelt(root, "content", None, {"type": "xhtml"})
    main_div_elt = xmlelt(content_elt, "div", None, {
                          "xmlns": "http://www.w3.org/1999/xhtml"})
    article_elt = xmlelt(main_div_elt, "article", None, None)
    div_elt = xmlelt(article_elt, "div", None, None)

    # Fichier a telecharger
    make_download_section(div_elt, entry)
    
    # raw text in a div html
    if "text" in entry and entry["text"]:
        elt = lxml.etree.fromstring("<div>{}</div>".format(entry["text"]))
        article_elt.append(elt)
    # insert html content
    if "html" in entry and entry["html"]:
        elt = lxml.etree.fromstring(entry["html"])
        article_elt.append(elt)

    return content_elt

def make_download_section(xml_node, entry):
    _download_files = []
    # si des fichiers avec proprietes etendues sont disponibles
    if 'files_props' in entry and entry['files_props']:
        for link in entry['files_props']:
            if 'type' in link and link['type']=='data':
                _available = ''
                _href = link['url']
                # fichier non disponible sur le serveur : statut http 404
                if link['http_status'] == 404:
                    _available = '[INDISPONIBLE] '
                    _href = None

                _download_files.append(dict(text='{} {}({})'.format(
                    os.path.basename(link['url']), _available, helpers.file_size(int(link['size']))),
                    href=_href))
    else:
        if 'files' in entry and entry['files']:
            for link in entry['files']:
                _download_files.append(dict(text=os.path.basename(link), href=link))

    
    suffix = ''
    if len(_download_files) > 1:
        suffix = 's'
    xmlelt(xml_node, "h1", u"{} Fichier{} à télécharger : ".format(len(_download_files), suffix))
    if len(_download_files):
        ul = xmlelt(xml_node, "ul")
        for fi in _download_files:
            if fi['href']:
                xmlelt(xmlelt(ul, "li"), "a", fi['text'], {"href": fi['href']})
            else:
                xmlelt(xmlelt(ul, "li"), None, fi['text'])

def xml2text(elem, encoding='utf-8', xml_decl=True):
    """
        Retourne une version indentée de l'arbre XML
    :param encoding:
    :param elem: noeud de l'arbre XML
    :return: Texte avec XML indenté
    """
    # rough_string = xml.etree.ElementTree.tostring(elem, encoding=encoding)
    # reparsed = minidom.parseString(rough_string)
    # return reparsed.toprettyxml(indent="  ")

    data = lxml.etree.tostring(elem, encoding=encoding,
                               pretty_print=True,
                               xml_declaration=xml_decl)
    return data.decode(encoding)


def xmlelt(parent, tag, text=None, attrs=None):
    """
    Production d'un noeud XML avec positionnement des attributs

    :param attrs:
    :param text:
    :param parent: parent de l'element XML
    :param tag: balise
    :return: element cree
    """

    if tag:
        if parent is None:
            elem = Element(tag)
        else:
            elem = SubElement(parent, tag)
    else:
        elem = parent

    if text:
        elem.text = text

    if attrs:
        for (k, v) in attrs.items():
            elem.attrib[k] = v

    return elem
