# -*- coding: utf-8 -*-
from cwr.agreement import AgreementRecord, InterestedPartyForAgreementRecord
from cwr.interested_party import Publisher, Writer
from cwr.work import WorkRecord, AlternateTitleRecord, AuthoredWorkRecord, \
    RecordingDetailRecord, WorkOriginRecord, PerformingArtistRecord

"""
Offers methods to create model objects from JSON objects.
"""

__author__ = 'Bernardo Martínez Garrido, Borja Garrido Bear'
__license__ = 'MIT'
__status__ = 'Development'


def parse_agreement(json_item):
    """
    Creates an Agreement from the data stored in a JSON object, and adds to it the specified submitter ID.

    :param json_item: JSON object to parse
    :return: an Agreement parsed from the JSON and with the specified id
    """
    # TODO Optional fields may be missing on the JSON
    agreement = AgreementRecord(record_type='', transaction_sequence_n=0, record_sequence_n=0,
                                submitter_agreement_n=json_item['submitter_agreement_number'],
                                society_assigned_agreement_n=json_item['society_agreement_number'],
                                agreement_type=json_item['agreement_type'],
                                agreement_start_date=json_item['start_date'],
                                agreement_end_date=json_item['end_date'],
                                prior_royalty_status=json_item['prior_royalty_status'],
                                post_term_collection_status=json_item['post_term_collection_status'],
                                date_of_signature=json_item['signature_date'],
                                number_of_works=json_item['works_number'],
                                sales_manufacture_clause=json_item['sales_manufacture_clause'],
                                international_standard_code=json_item['international_standard_code'],
                                retention_end_date=json_item['retention_end_date'],
                                prior_royalty_start_date=json_item['prior_royalty_start_date'],
                                post_term_collection_end_date=json_item['post_term_collection_end_date'],
                                shares_change=json_item['shares_change'],
                                advance_given=json_item['advance_given'])

    return agreement


def parse_alternative_work_title(json_item):
    """
    Creates an AlternativeWorkTitle from the data stored in a JSON object.

    :param json_item: JSON object to parse
    :return: an AlternativeWorkTitle parsed from the JSON
    """
    title = AlternateTitleRecord('', 0, 0, json_item['alternate_title'],
                                 json_item['title_type'],
                                 json_item['language'])

    return title


def parse_authored_work(json_item):
    """
    Creates an AuthoredWork from the data stored in a JSON object.

    :param json_item: JSON object to parse
    :return: an AuthoredWork parsed from the JSON
    """
    title = AuthoredWorkRecord('', 0, 0, submitter_work_n=json_item['work_id'],
                               title=json_item['title'],
                               language_code=json_item['language_code'],
                               source=json_item['source'],
                               writer_1_first_name=json_item['first_name_1'],
                               writer_1_ipi_base_n=json_item['ipi_base_1'],
                               writer_1_ipi_name_n=json_item['ipi_name_1'],
                               writer_2_first_name=json_item['first_name_2'],
                               writer_2_ipi_base_n=json_item['ipi_base_2'],
                               writer_2_ipi_name_n=json_item['ipi_name_2'],
                               writer_1_last_name=json_item['last_name_1'],
                               writer_2_last_name=json_item['last_name_2'],
                               iswc=json_item['iswc'])

    return title


def parse_ipa(json_item):
    """
    Creates an IPA from the data stored in a JSON object, and adds to it the specified submitter ID.

    :param json_item: JSON object to parse
    :return: an IPA parsed from the JSON
    """
    agreement = InterestedPartyForAgreementRecord('', 0, 0, json_item['ip_id'], json_item['ip_last_name'],
                                                  json_item['agreement_role_code'], json_item['ip_writer_name'],
                                                  json_item['ip_ipi'], json_item['ipi_name'], json_item['pr_society'],
                                                  json_item['pr_share'],
                                                  json_item['mr_society'], json_item['mr_share'],
                                                  json_item['sr_society'],
                                                  json_item['sr_share'])

    return agreement


def parse_performing_artist(json_item):
    """
    Creates a PerformingArtist from the data stored in a JSON object.

    :param json_item: JSON object to parse
    :return: a PerformingArtist parsed from the JSON
    """
    artist = PerformingArtistRecord('', 0, 0, json_item['last_name'],
                                    json_item['first_name'],
                                    json_item['ipi_name'],
                                    json_item['ipi_base_number'])

    return artist


def parse_publisher(json_item):
    """
    Creates an InterestedParty from the data stored in a JSON object, and adds to it the specified submitter ID.

    :param json_item: JSON object to parse
    :return: an InterestedParty parsed from the JSON and with the specified id
    """
    publisher = Publisher(json_item['publisher_id'],
                          json_item['name'],
                          json_item['ipi_base_id'],
                          json_item['tax_id'],
                          json_item['ipi_name'])

    return publisher


def parse_recording_details(json_item):
    """
    Creates a RecordingDetails from the data stored in a JSON object.

    :param json_item: JSON object to parse
    :return: a RecordingDetails parsed from the JSON
    """
    details = RecordingDetailRecord('', 0, 0, json_item['first_release_date'],
                                    json_item['first_release_duration'],
                                    json_item['first_album_title'],
                                    json_item['first_album_label'],
                                    json_item['first_release_catalog_id'],
                                    json_item['ean'],
                                    json_item['isrc'],
                                    json_item['recording_format'],
                                    json_item['recording_technique'],
                                    json_item['media_type'])

    return details


def parse_work(json_item):
    """
    Creates a Work from the data stored in a JSON object, and adds to it the specified submitter ID.

    :param json_item: JSON object to parse
    :return: a Work parsed from the JSON and with the specified id
    """
    work = WorkRecord('', 0, 0, submitter_work_n=json_item['work_id'], title=json_item['title'],
                      language_code=json_item['language_code'],
                      date_publication_printed_edition=json_item['printed_edition_publication_date'],
                      copyright_number=json_item['copyright_number'],
                      copyright_date=json_item['copyright_date'],
                      text_music_relationship=json_item['text_music_relationship'],
                      version_type=json_item['version_type'],
                      music_arrangement=json_item['music_arrangement'], lyric_adaptation=json_item['lyric_adaptation'],
                      excerpt_type=json_item['excerpt_type'],
                      composite_type=json_item['composite_type'],
                      composite_component_count=json_item['composite_component_count'], iswc=json_item['iswc'],
                      work_type=json_item['cwr_work_type'],
                      musical_work_distribution_category=json_item['musical_distribution_category'],
                      duration=json_item['duration'], catalogue_number=json_item['catalogue_number'],
                      opus_number=json_item['opus_number'],
                      contact_id=json_item['contact_id'], contact_name=json_item['contact_name'],
                      recorded_indicator=json_item['recorded_indicator'],
                      priority_flag=json_item['priority_flag'], exceptional_clause=json_item['exceptional_clause'],
                      grand_rights_indicator=json_item['grand_rights_indicator'])

    return work


def parse_work_origin(json_item):
    """
    Creates a WorkOrigin from the data stored in a JSON object.

    :param json_item: JSON object to parse
    :return: a WorkOrigin parsed from the JSON
    """
    origin = WorkOriginRecord('', 0, 0, json_item['intended_purpose'],
                              json_item['production_title'],
                              json_item['cd_identifier'],
                              json_item['cut_number'],
                              json_item['library'],
                              json_item['blt'],
                              json_item['visan_version'],
                              json_item['visan_isan'],
                              json_item['visan_episode'],
                              json_item['visan_check_digit'],
                              json_item['production_id'],
                              json_item['episode_title'])

    return origin


def parse_writer(json_item):
    """
    Creates a Writer from the data stored in a JSON object, and adds to it the specified submitter ID.

    :param json_item: JSON object to parse
    :return: a Writer parsed from the JSON and with the specified id
    """
    writer = Writer(json_item['first_name'],
                    json_item['personal_number'], json_item['ip_id'],
                    json_item['ip_name'], json_item['ip_base_id'],
                    json_item['last_name'])

    return writer