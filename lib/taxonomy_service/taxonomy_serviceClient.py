# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class taxonomy_service(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def search_taxonomy(self, params, context=None):
        """
        :param params: instance of type "DropDownItemInputParams" ->
           structure: parameter "private" of Long, parameter "public" of
           Long, parameter "local" of Long, parameter "search" of String,
           parameter "limit" of Long, parameter "start" of Long, parameter
           "workspace" of String
        :returns: instance of type "DropDownData" -> structure: parameter
           "num_of_hits" of Long, parameter "hits" of list of type
           "DropDownItem" -> structure: parameter "label" of String,
           parameter "id" of String, parameter "category" of String,
           parameter "parent" of String, parameter "parent_ref" of String
        """
        return self._client.call_method(
            'taxonomy_service.search_taxonomy',
            [params], self._service_ver, context)

    def create_taxonomy(self, params, context=None):
        """
        :param params: instance of type "CreateTaxonomyInputParams" ->
           structure: parameter "scientific_name" of String, parameter
           "taxonomic_id" of Long, parameter "kingdom" of String, parameter
           "domain" of String, parameter "rank" of String, parameter
           "comments" of String, parameter "genetic_code" of String,
           parameter "aliases" of list of String, parameter "workspace" of
           String
        :returns: instance of type "CreateTaxonomyOut" -> structure:
           parameter "ref" of type "ObjectReference" (workspace ref to an
           object), parameter "scientific_name" of String
        """
        return self._client.call_method(
            'taxonomy_service.create_taxonomy',
            [params], self._service_ver, context)

    def change_taxa(self, params, context=None):
        """
        :param params: instance of type "ChangeTaxaInputParams" -> structure:
           parameter "input_genome" of String, parameter "scientific_name" of
           String, parameter "workspace" of String, parameter "output_genome"
           of String
        :returns: instance of type "ChangeTaxaOut" -> structure: parameter
           "genome_ref" of String, parameter "taxa_ref" of String, parameter
           "genome_name" of String
        """
        return self._client.call_method(
            'taxonomy_service.change_taxa',
            [params], self._service_ver, context)

    def get_taxonomies_by_id(self, params, context=None):
        """
        :param params: instance of type "GetTaxonomiesIdInputParams" ->
           structure: parameter "taxonomy_object_refs" of list of type
           "ObjectReference" (workspace ref to an object)
        :returns: instance of type "GetTaxonomiesOut" -> structure: parameter
           "taxa_ref" of String, parameter "lineage_genomes" of list of type
           "lineage_steps" -> structure: parameter "lineage_step" of String,
           parameter "lineage_count" of Long
        """
        return self._client.call_method(
            'taxonomy_service.get_taxonomies_by_id',
            [params], self._service_ver, context)

    def get_genomes_for_taxonomy(self, params, context=None):
        """
        :param params: instance of type "GetGenomesTaxonomyInputParams" ->
           structure: parameter "taxa_ref" of String
        :returns: instance of type "GetTaxonomiesOut" -> structure: parameter
           "taxa_ref" of String, parameter "lineage_genomes" of list of type
           "lineage_steps" -> structure: parameter "lineage_step" of String,
           parameter "lineage_count" of Long
        """
        return self._client.call_method(
            'taxonomy_service.get_genomes_for_taxonomy',
            [params], self._service_ver, context)

    def get_genomes_for_taxa_group(self, params, context=None):
        """
        :param params: instance of type "GetGenomesTaxaGroupInputParams" ->
           structure: parameter "start" of Long, parameter "limit" of Long,
           parameter "lineage_step" of String
        :returns: instance of type "GetGenomesOut" -> structure: parameter
           "lineage_step" of String, parameter "lineage_count" of Long,
           parameter "TaxaInfo" of list of type "TaxaViewerOutput" ->
           structure: parameter "scientific_name" of String, parameter
           "kingdom" of String, parameter "ws_ref" of String, parameter
           "parent_taxon_ref" of String, parameter "deleted" of Long,
           parameter "aliases" of list of String, parameter
           "scientific_lineage" of String
        """
        return self._client.call_method(
            'taxonomy_service.get_genomes_for_taxa_group',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('taxonomy_service.status',
                                        [], self._service_ver, context)
