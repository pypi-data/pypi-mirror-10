# -*- coding: utf-8 -*-

from cwr.acknowledgement import *
from cwr.agreement import *
from cwr.group import *
from cwr.info import *
from cwr.parser.encoder.common import Encoder
from cwr.interested_party import *
from cwr.non_roman_alphabet import *
from cwr.transmission import *
from cwr.work import *
from cwr.file import *
from cwr.other import *
from cwr.table_value import *


"""
Classes for transforming instances of the CWR model into dictionaries.

A single monolithic encoder takes care of this process. It will just check the class of the received object and encode
it accordingly.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class CWRDictionaryEncoder(Encoder):
    """
    Encodes CWR model classes into dictionaries.

    It will check the class of the received class, and encode it accordingly.
    """

    def __init__(self):
        super(CWRDictionaryEncoder, self).__init__()

    def encode(self, object):
        if isinstance(object, AcknowledgementRecord):
            # Acknowledgement
            encoded = self.__encode_acknowledgement_record(object)
        elif isinstance(object, AdditionalRelatedInfoRecord):
            # Additional Related Info
            encoded = self.__encode_additional_related_info_record(object)
        elif isinstance(object, AgreementRecord):
            # Agreement
            encoded = self.__encode_agreement_record(object)
        elif isinstance(object, AgreementTerritoryRecord):
            # Agreement Territory
            encoded = self.__encode_agreement_territory_record(object)
        elif isinstance(object, AlternateTitleRecord):
            # Alternate Title
            encoded = self.__encode_alternate_title_record(object)
        elif isinstance(object, AuthoredWorkRecord):
            # Authored Work
            encoded = self.__encode_authored_work_record(object)
        elif isinstance(object, ComponentRecord):
            # Component
            encoded = self.__encode_component_record(object)
        elif isinstance(object, Group):
            # Group
            encoded = self.__encode_group(object)
        elif isinstance(object, GroupHeader):
            # Group Header
            encoded = self.__encode_group_header(object)
        elif isinstance(object, GroupTrailer):
            # Group Trailer
            encoded = self.__encode_group_trailer(object)
        elif isinstance(object, InstrumentationDetailRecord):
            # Instrumentation Detail
            encoded = self.__encode_instrumentation_detail_record(object)
        elif isinstance(object, InstrumentationSummaryRecord):
            # Instrumentation Summary
            encoded = self.__encode_instrumentation_summary_record(object)
        elif isinstance(object, InterestedPartyForAgreementRecord):
            # Interested Party for Agreement
            encoded = self.__encode_interested_party_agreement_record(object)
        elif isinstance(object, IPTerritoryOfControlRecord):
            # Interested Party (Writer/Publisher) Territory of Control
            encoded = self.__encode_interested_party_territory_control_record(object)
        elif isinstance(object, MessageRecord):
            # Message
            encoded = self.__encode_message_record(object)
        elif isinstance(object, NonRomanAlphabetTitleRecord):
            # NAT Record
            encoded = self.__encode_nat_record(object)
        elif isinstance(object, NonRomanAlphabetOtherWriterRecord):
            # NOW Record
            encoded = self.__encode_now_record(object)
        elif isinstance(object, NonRomanAlphabetAgreementPartyRecord):
            # NPA Record
            encoded = self.__encode_npa_record(object)
        elif isinstance(object, NonRomanAlphabetPublisherNameRecord):
            # NPN Record
            encoded = self.__encode_npn_record(object)
        elif isinstance(object, NonRomanAlphabetPerformanceDataRecord):
            # NPR Record
            encoded = self.__encode_npr_record(object)
        elif isinstance(object, NonRomanAlphabetWorkRecord):
            # NRA Record for Works
            encoded = self.__encode_nra_work_record(object)
        elif isinstance(object, NonRomanAlphabetWriterNameRecord):
            # NWN Record for Works
            encoded = self.__encode_nwn_record(object)
        elif isinstance(object, PerformingArtistRecord):
            # Performing Artist
            encoded = self.__encode_performing_artist_record(object)
        elif isinstance(object, Publisher):
            # Publisher IP
            encoded = self.__encode_publisher(object)
        elif isinstance(object, PublisherForWriterRecord):
            # Publisher For Writer
            encoded = self.__encode_publisher_for_writer_record(object)
        elif isinstance(object, PublisherRecord):
            # Publisher
            encoded = self.__encode_publisher_record(object)
        elif isinstance(object, RecordingDetailRecord):
            # Recording Detail
            encoded = self.__encode_recording_detail_record(object)
        elif isinstance(object, Transmission):
            # Transmission
            encoded = self.__encode_transmission(object)
        elif isinstance(object, TransmissionHeader):
            # Transmission Header
            encoded = self.__encode_transmission_header(object)
        elif isinstance(object, TransmissionTrailer):
            # Transmission Trailer
            encoded = self.__encode_transmission_trailer(object)
        elif isinstance(object, WorkRecord):
            # Work
            encoded = self.__encode_work_record(object)
        elif isinstance(object, WorkOriginRecord):
            # Work Origin
            encoded = self.__encode_work_origin_record(object)
        elif isinstance(object, Writer):
            # Writer IP
            encoded = self.__encode_writer(object)
        elif isinstance(object, WriterRecord):
            # Writer
            encoded = self.__encode_writer_record(object)
        elif isinstance(object, ISWCCode):
            # ISWC
            encoded = self.__encode_iswc(object)
        elif isinstance(object, IPIBaseNumber):
            # IPI Base Number
            encoded = self.__encode_ipi_base(object)
        elif isinstance(object, VISAN):
            # V-ISAN
            encoded = self.__encode_visan(object)
        elif isinstance(object, AVIKey):
            # AVI Key
            encoded = self.__encode_avi_key(object)
        elif isinstance(object, MediaTypeValue):
            # Media type value
            encoded = self.__encode_media_type_value(object)
        elif isinstance(object, InstrumentValue):
            # Instrument value
            encoded = self.__encode_instrument_value(object)
        elif isinstance(object, TableValue):
            # Table value
            encoded = self.__encode_table_value(object)
        elif isinstance(object, FileTag):
            # Table value
            encoded = self.__encode_file_tag(object)
        elif isinstance(object, CWRFile):
            # Table value
            encoded = self.__encode_file(object)
        else:
            encoded = None

        return encoded

    def __encode_transaction_record_head(self, record):
        """
        Creates the head of a transaction record.

        :param record: the record with the head to transform into a dictionary
        :return: a dictionary created from the record head
        """
        encoded = {}

        encoded['record_type'] = record.record_type
        encoded['transaction_sequence_n'] = record.transaction_sequence_n
        encoded['record_sequence_n'] = record.record_sequence_n

        return encoded

    def __encode_interested_party(self, record):
        """
        Creates a dictionary from an InterestedParty.

        :param record: the InterestedParty to transform into a dictionary
        :return: a dictionary created from the InterestedParty
        """
        encoded = {}

        encoded['ip_n'] = record.ip_n
        encoded['ipi_base_n'] = record.ipi_base_n
        encoded['ipi_name_n'] = record.ipi_name_n
        encoded['tax_id'] = record.tax_id

        return encoded

    def __encode_interested_party_record(self, record):
        """
        Creates a dictionary from a InterestedPartyRecord.

        :param record: the InterestedPartyRecord to transform into a dictionary
        :return: a dictionary created from the InterestedPartyRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['first_recording_refusal'] = record.first_recording_refusal
        encoded['pr_society'] = record.pr_society
        encoded['pr_ownership_share'] = record.pr_ownership_share
        encoded['mr_society'] = record.mr_society
        encoded['mr_ownership_share'] = record.mr_ownership_share
        encoded['sr_society'] = record.sr_society
        encoded['sr_ownership_share'] = record.sr_ownership_share
        encoded['usa_license'] = record.usa_license

        return encoded

    def __encode_nra_record(self, record):
        """
        Creates a dictionary from a NRARecord.

        :param record: the NRARecord to transform into a dictionary
        :return: a dictionary created from the NRARecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['language_code'] = record.language_code

        return encoded

    def __encode_base_work_record(self, record):
        """
        Creates a dictionary from a BaseWorkRecord.

        :param record: the BaseWorkRecord to transform into a dictionary
        :return: a dictionary created from the BaseWorkRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['iswc'] = self.encode(record.iswc)
        encoded['language_code'] = record.language_code
        encoded['title'] = record.title

        return encoded

    def __encode_acknowledgement_record(self, record):
        """
        Creates a dictionary from an AcknowledgementRecord.

        :param record: the AcknowledgementRecord to transform into a dictionary
        :return: a dictionary created from the AcknowledgementRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['creation_date_time'] = record.creation_date_time
        encoded['creation_title'] = record.creation_title
        encoded['original_group_id'] = record.original_group_id
        encoded['original_transaction_sequence_n'] = record.original_transaction_sequence_n
        encoded['original_transaction_type'] = record.original_transaction_type
        encoded['processing_date'] = record.processing_date
        encoded['recipient_creation_n'] = record.recipient_creation_n
        encoded['submitter_creation_n'] = record.submitter_creation_n
        encoded['transaction_status'] = record.transaction_status

        return encoded

    def __encode_additional_related_info_record(self, record):
        """
        Creates a dictionary from an AdditionalRelatedInfoRecord.

        :param record: the AdditionalRelatedInfoRecord to transform into a dictionary
        :return: a dictionary created from the AdditionalRelatedInfoRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['note'] = record.note
        encoded['society_n'] = record.society_n
        encoded['subject_code'] = record.subject_code
        encoded['type_of_right'] = record.type_of_right
        encoded['work_n'] = record.work_n

        return encoded

    def __encode_agreement_record(self, record):
        """
        Creates a dictionary from an AgreementRecord.

        :param record: the AgreementRecord to transform into a dictionary
        :return: a dictionary created from the AgreementRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['advance_given'] = record.advance_given
        encoded['agreement_end_date'] = record.agreement_end_date
        encoded['date_of_signature'] = record.date_of_signature
        encoded['agreement_start_date'] = record.agreement_start_date
        encoded['agreement_type'] = record.agreement_type
        encoded['international_standard_code'] = record.international_standard_code
        encoded['number_of_works'] = record.number_of_works
        encoded['post_term_collection_end_date'] = record.post_term_collection_end_date
        encoded['post_term_collection_status'] = record.post_term_collection_status
        encoded['prior_royalty_start_date'] = record.prior_royalty_start_date
        encoded['prior_royalty_status'] = record.prior_royalty_status
        encoded['retention_end_date'] = record.retention_end_date
        encoded['sales_manufacture_clause'] = record.sales_manufacture_clause
        encoded['shares_change'] = record.shares_change
        encoded['society_assigned_agreement_n'] = record.society_assigned_agreement_n
        encoded['submitter_agreement_n'] = record.submitter_agreement_n

        return encoded

    def __encode_agreement_territory_record(self, record):
        """
        Creates a dictionary from an AgreementTerritoryRecord.

        :param record: the AgreementTerritoryRecord to transform into a dictionary
        :return: a dictionary created from the AgreementTerritoryRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['inclusion_exclusion_indicator'] = record.inclusion_exclusion_indicator
        encoded['tis_numeric_code'] = record.tis_numeric_code

        return encoded

    def __encode_alternate_title_record(self, record):
        """
        Creates a dictionary from an AlternateTitleRecord.

        :param record: the AlternateTitleRecord to transform into a dictionary
        :return: a dictionary created from the AlternateTitleRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['alternate_title'] = record.alternate_title
        encoded['title_type'] = record.title_type
        encoded['language_code'] = record.language_code

        return encoded

    def __encode_authored_work_record(self, record):
        """
        Creates a dictionary from an AuthoredWorkRecord.

        :param record: the AuthoredWorkRecord to transform into a dictionary
        :return: a dictionary created from the AuthoredWorkRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['iswc'] = self.encode(record.iswc)
        encoded['language_code'] = record.language_code
        encoded['source'] = record.source
        encoded['submitter_work_n'] = record.submitter_work_n
        encoded['title'] = record.title
        encoded['writer_1_first_name'] = record.writer_1_first_name
        encoded['writer_2_first_name'] = record.writer_2_first_name
        encoded['writer_1_ipi_base_n'] = record.writer_1_ipi_base_n
        encoded['writer_2_ipi_base_n'] = record.writer_2_ipi_base_n
        encoded['writer_1_ipi_name_n'] = record.writer_1_ipi_name_n
        encoded['writer_2_ipi_name_n'] = record.writer_2_ipi_name_n
        encoded['writer_1_last_name'] = record.writer_1_last_name
        encoded['writer_2_last_name'] = record.writer_2_last_name

        return encoded

    def __encode_component_record(self, record):
        """
        Creates a dictionary from an ComponentRecord.

        :param record: the ComponentRecord to transform into a dictionary
        :return: a dictionary created from the ComponentRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['duration'] = record.duration
        encoded['iswc'] = self.encode(record.iswc)
        encoded['submitter_work_n'] = record.submitter_work_n
        encoded['title'] = record.title
        encoded['writer_1_first_name'] = record.writer_1_first_name
        encoded['writer_2_first_name'] = record.writer_2_first_name
        encoded['writer_2_ipi_base_n'] = record.writer_2_ipi_base_n
        encoded['writer_2_ipi_name_n'] = record.writer_2_ipi_name_n
        encoded['writer_1_ipi_base_n'] = record.writer_1_ipi_base_n
        encoded['writer_1_ipi_name_n'] = record.writer_1_ipi_name_n
        encoded['writer_1_last_name'] = record.writer_1_last_name
        encoded['writer_2_last_name'] = record.writer_2_last_name

        return encoded

    def __encode_group(self, record):
        """
        Creates a dictionary from an Group.

        :param record: the Group to transform into a dictionary
        :return: a dictionary created from the Group
        """
        encoded = {}

        encoded['group_header'] = self.encode(record.group_header)
        encoded['group_trailer'] = self.encode(record.group_trailer)

        transactions = []
        for trs in record.transactions:
            transaction = []
            for tr in trs:
                transaction.append(self.encode(tr))
            transactions.append(transaction)

        encoded['transactions'] = transactions

        return encoded

    def __encode_group_header(self, record):
        """
        Creates a dictionary from an GroupHeader.

        :param record: the GroupHeader to transform into a dictionary
        :return: a dictionary created from the GroupHeader
        """
        encoded = {}

        encoded['batch_request_id'] = record.batch_request_id
        encoded['group_id'] = record.group_id
        encoded['record_type'] = record.record_type
        encoded['transaction_type'] = record.transaction_type
        encoded['version_number'] = record.version_number

        return encoded

    def __encode_group_trailer(self, record):
        """
        Creates a dictionary from an GroupTrailer.

        :param record: the GroupTrailer to transform into a dictionary
        :return: a dictionary created from the GroupTrailer
        """
        encoded = {}

        encoded['group_id'] = record.group_id
        encoded['record_count'] = record.record_count
        encoded['record_type'] = record.record_type
        encoded['transaction_count'] = record.transaction_count

        return encoded

    def __encode_instrumentation_detail_record(self, record):
        """
        Creates a dictionary from an InstrumentationDetailRecord.

        :param record: the InstrumentationDetailRecord to transform into a dictionary
        :return: a dictionary created from the InstrumentationDetailRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['instrument_code'] = record.instrument_code
        encoded['number_players'] = record.number_players

        return encoded

    def __encode_instrumentation_summary_record(self, record):
        """
        Creates a dictionary from an InstrumentationSummaryRecord.

        :param record: the InstrumentationSummaryRecord to transform into a dictionary
        :return: a dictionary created from the InstrumentationSummaryRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['instrumentation_description'] = record.instrumentation_description
        encoded['number_voices'] = record.number_voices
        encoded['standard_instrumentation_type'] = record.standard_instrumentation_type

        return encoded

    def __encode_interested_party_agreement_record(self, record):
        """
        Creates a dictionary from an AgreementInterestedParty.

        :param record: the AgreementInterestedParty to transform into a dictionary
        :return: a dictionary created from the AgreementInterestedParty
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['agreement_role_code'] = record.agreement_role_code
        encoded['ip_last_name'] = record.ip_last_name
        encoded['ip_n'] = record.ip_n
        encoded['ip_writer_first_name'] = record.ip_writer_first_name
        encoded['ipi_name_n'] = record.ipi_name_n
        encoded['ipi_base_n'] = record.ipi_base_n
        encoded['mr_society'] = record.mr_society
        encoded['mr_share'] = record.mr_share
        encoded['pr_society'] = record.pr_society
        encoded['pr_share'] = record.pr_share
        encoded['sr_society'] = record.sr_society
        encoded['sr_share'] = record.sr_share

        return encoded

    def __encode_interested_party_territory_control_record(self, record):
        """
        Creates a dictionary from an IPTerritoryOfControlRecord.

        :param record: the IPTerritoryOfControlRecord to transform into a dictionary
        :return: a dictionary created from the IPTerritoryOfControlRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['ip_n'] = record.ip_n
        encoded['ie_indicator'] = record.inclusion_exclusion_indicator
        encoded['tis_numeric_code'] = record.tis_numeric_code
        encoded['sequence_n'] = record.sequence_n
        encoded['pr_collection_share'] = record.pr_collection_share
        encoded['mr_collection_share'] = record.mr_collection_share
        encoded['sr_collection_share'] = record.sr_collection_share
        encoded['shares_change'] = record.shares_change

        return encoded

    def __encode_message_record(self, record):
        """
        Creates a dictionary from a MessageRecord.

        :param record: the MessageRecord to transform into a dictionary
        :return: a dictionary created from the MessageRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['message_level'] = record.message_level
        encoded['message_record_type'] = record.message_record_type
        encoded['message_text'] = record.message_text
        encoded['message_type'] = record.message_type
        encoded['original_record_sequence_n'] = record.original_record_sequence_n
        encoded['validation_n'] = record.validation_n

        return encoded

    def __encode_nat_record(self, record):
        """
        Creates a dictionary from a NATRecord.

        :param record: the NATRecord to transform into a dictionary
        :return: a dictionary created from the NATRecord
        """
        encoded = self.__encode_nra_record(record)

        encoded['title'] = record.title
        encoded['title_type'] = record.title_type

        return encoded

    def __encode_now_record(self, record):
        """
        Creates a dictionary from a NOWRecord.

        :param record: the NOWRecord to transform into a dictionary
        :return: a dictionary created from the NOWRecord
        """
        encoded = self.__encode_nra_record(record)

        encoded['position'] = record.position
        encoded['writer_first_name'] = record.writer_first_name
        encoded['writer_name'] = record.writer_name

        return encoded

    def __encode_npa_record(self, record):
        """
        Creates a dictionary from a NPARecord.

        :param record: the NPARecord to transform into a dictionary
        :return: a dictionary created from the NPARecord
        """
        encoded = self.__encode_nra_record(record)

        encoded['ip_name'] = record.ip_name
        encoded['ip_writer_name'] = record.ip_writer_name
        encoded['ip_n'] = record.ip_n

        return encoded

    def __encode_npn_record(self, record):
        """
        Creates a dictionary from a NPNRecord.

        :param record: the NPNRecord to transform into a dictionary
        :return: a dictionary created from the NPNRecord
        """
        encoded = self.__encode_nra_record(record)

        encoded['ip_n'] = record.ip_n
        encoded['publisher_name'] = record.publisher_name
        encoded['publisher_sequence_n'] = record.publisher_sequence_n

        return encoded

    def __encode_npr_record(self, record):
        """
        Creates a dictionary from a NPRRecord.

        :param record: the NPRRecord to transform into a dictionary
        :return: a dictionary created from the NPRRecord
        """
        encoded = self.__encode_nra_record(record)

        encoded['performance_dialect'] = record.performance_dialect
        encoded['performance_language'] = record.performance_language
        encoded['performing_artist_first_name'] = record.performing_artist_first_name
        encoded['performing_artist_ipi_base_n'] = record.performing_artist_ipi_base_n
        encoded['performing_artist_ipi_name_n'] = record.performing_artist_ipi_name_n
        encoded['performing_artist_name'] = record.performing_artist_name

        return encoded

    def __encode_nra_work_record(self, record):
        """
        Creates a dictionary from a NRAWorkRecord.

        :param record: the NRAWorkRecord to transform into a dictionary
        :return: a dictionary created from the NRAWorkRecord
        """
        encoded = self.__encode_nra_record(record)

        encoded['title'] = record.title

        return encoded

    def __encode_publisher(self, record):
        """
        Creates a dictionary from a Publisher.

        :param record: the Publisher to transform into a dictionary
        :return: a dictionary created from the Publisher
        """
        encoded = self.__encode_interested_party(record)

        encoded['publisher_name'] = record.publisher_name

        return encoded

    def __encode_nwn_record(self, record):
        """
        Creates a dictionary from a NWNRecord.

        :param record: the NWNRecord to transform into a dictionary
        :return: a dictionary created from the NWNRecord
        """
        encoded = self.__encode_nra_record(record)

        encoded['writer_first_name'] = record.writer_first_name
        encoded['writer_last_name'] = record.writer_last_name
        encoded['ip_n'] = record.ip_n

        return encoded

    def __encode_performing_artist_record(self, record):
        """
        Creates a dictionary from a PerformingArtistRecord.

        :param record: the PerformingArtistRecord to transform into a dictionary
        :return: a dictionary created from the PerformingArtistRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['performing_artist_first_name'] = record.performing_artist_first_name
        encoded['performing_artist_ipi_base_n'] = record.performing_artist_ipi_base_n
        encoded['performing_artist_ipi_name_n'] = record.performing_artist_ipi_name_n
        encoded['performing_artist_last_name'] = record.performing_artist_last_name

        return encoded

    def __encode_publisher_for_writer_record(self, record):
        """
        Creates a dictionary from a PublisherForWriterRecord.

        :param record: the PublisherForWriterRecord to transform into a dictionary
        :return: a dictionary created from the PublisherForWriterRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['publisher_ip_n'] = record.publisher_ip_n
        encoded['society_assigned_agreement_n'] = record.society_assigned_agreement_n
        encoded['submitter_agreement_n'] = record.submitter_agreement_n
        encoded['writer_ip_n'] = record.writer_ip_n

        return encoded

    def __encode_publisher_record(self, record):
        """
        Creates a dictionary from a PublisherRecord.

        :param record: the PublisherRecord to transform into a dictionary
        :return: a dictionary created from the PublisherRecord
        """
        encoded = self.__encode_interested_party_record(record)

        encoded['agreement_type'] = record.agreement_type
        encoded['international_standard_code'] = record.international_standard_code
        encoded['pr_society'] = record.pr_society
        encoded['pr_ownership_share'] = record.pr_ownership_share
        encoded['publisher_sequence_n'] = record.publisher_sequence_n
        encoded['publisher_type'] = record.publisher_type
        encoded['publisher_unknown'] = record.publisher_unknown
        encoded['society_assigned_agreement_n'] = record.society_assigned_agreement_n
        encoded['special_agreements'] = record.special_agreements
        encoded['submitter_agreement_n'] = record.submitter_agreement_n

        encoded['publisher'] = self.encode(record.publisher)

        return encoded

    def __encode_recording_detail_record(self, record):
        """
        Creates a dictionary from a RecordingDetailRecord.

        :param record: the RecordingDetailRecord to transform into a dictionary
        :return: a dictionary created from the RecordingDetailRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['ean'] = record.ean
        encoded['first_album_label'] = record.first_album_label
        encoded['first_album_title'] = record.first_album_title
        encoded['first_release_catalog_n'] = record.first_release_catalog_n
        encoded['first_release_date'] = record.first_release_date
        encoded['first_release_duration'] = record.first_release_duration
        encoded['isrc'] = record.isrc
        encoded['media_type'] = record.media_type
        encoded['recording_format'] = record.recording_format
        encoded['recording_technique'] = record.recording_technique

        return encoded

    def __encode_transmission(self, record):
        """
        Creates a dictionary from a Transmission.

        :param record: the Transmission to transform into a dictionary
        :return: a dictionary created from the Transmission
        """
        encoded = {}

        encoded['header'] = self.encode(record.header)
        encoded['trailer'] = self.encode(record.trailer)

        groups = []
        for g in record.groups:
            groups.append(self.encode(g))

        encoded['groups'] = groups

        return encoded

    def __encode_transmission_header(self, record):
        """
        Creates a dictionary from a TransmissionHeader.

        :param record: the TransmissionHeader to transform into a dictionary
        :return: a dictionary created from the TransmissionHeader
        """
        encoded = {}

        encoded['record_type'] = record.record_type
        encoded['sender_id'] = record.sender_id
        encoded['sender_name'] = record.sender_name
        encoded['sender_type'] = record.sender_type
        encoded['creation_date_time'] = record.creation_date_time
        encoded['transmission_date'] = record.transmission_date
        encoded['edi_standard'] = record.edi_standard
        encoded['character_set'] = record.character_set

        return encoded

    def __encode_transmission_trailer(self, record):
        """
        Creates a dictionary from a TransmissionTrailer.

        :param record: the TransmissionTrailer to transform into a dictionary
        :return: a dictionary created from the TransmissionTrailer
        """
        encoded = {}

        encoded['record_type'] = record.record_type
        encoded['group_count'] = record.group_count
        encoded['transaction_count'] = record.transaction_count
        encoded['record_count'] = record.record_count

        return encoded

    def __encode_work_record(self, record):
        """
        Creates a dictionary from a WorkRecord.

        :param record: the WorkRecord to transform into a dictionary
        :return: a dictionary created from the WorkRecord
        """
        encoded = self.__encode_base_work_record(record)

        encoded['catalogue_number'] = record.catalogue_number
        encoded['composite_component_count'] = record.composite_component_count
        encoded['composite_type'] = record.composite_type
        encoded['contact_id'] = record.contact_id
        encoded['contact_name'] = record.contact_name
        encoded['copyright_date'] = record.copyright_date
        encoded['copyright_number'] = record.copyright_number
        encoded['work_type'] = record.work_type
        encoded['date_publication_printed_edition'] = record.date_publication_printed_edition
        encoded['duration'] = record.duration
        encoded['exceptional_clause'] = record.exceptional_clause
        encoded['excerpt_type'] = record.excerpt_type
        encoded['grand_rights_indicator'] = record.grand_rights_indicator
        encoded['lyric_adaptation'] = record.lyric_adaptation
        encoded['music_arrangement'] = record.music_arrangement
        encoded['musical_work_distribution_category'] = record.musical_work_distribution_category
        encoded['opus_number'] = record.opus_number
        encoded['priority_flag'] = record.priority_flag
        encoded['recorded_indicator'] = record.recorded_indicator
        encoded['submitter_work_n'] = record.submitter_work_n
        encoded['text_music_relationship'] = record.text_music_relationship
        encoded['version_type'] = record.version_type

        return encoded

    def __encode_work_origin_record(self, record):
        """
        Creates a dictionary from a WorkOriginRecord.

        :param record: the WorkOriginRecord to transform into a dictionary
        :return: a dictionary created from the WorkOriginRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['bltvr'] = record.bltvr
        encoded['cd_identifier'] = record.cd_identifier
        encoded['cut_number'] = record.cut_number
        encoded['episode_n'] = record.episode_n
        encoded['episode_title'] = record.episode_title
        encoded['intended_purpose'] = record.intended_purpose
        encoded['library'] = record.library
        encoded['production_n'] = record.production_n
        encoded['production_title'] = record.production_title
        encoded['year_production'] = record.year_production

        encoded['audio_visual_key'] = self.encode(record.audio_visual_key)
        encoded['visan'] = self.encode(record.visan)

        return encoded

    def __encode_writer(self, record):
        """
        Creates a dictionary from a Writer.

        :param record: the Writer to transform into a dictionary
        :return: a dictionary created from the Writer
        """
        encoded = self.__encode_interested_party(record)

        encoded['personal_number'] = record.personal_number
        encoded['writer_first_name'] = record.writer_first_name
        encoded['writer_last_name'] = record.writer_last_name

        return encoded

    def __encode_writer_record(self, record):
        """
        Creates a dictionary from a WriterRecord.

        :param record: the WriterRecord to transform into a dictionary
        :return: a dictionary created from the WriterRecord
        """
        encoded = self.__encode_interested_party_record(record)

        encoded['reversionary'] = record.reversionary
        encoded['writer_designation'] = record.writer_designation
        encoded['writer_unknown'] = record.writer_unknown
        encoded['work_for_hire'] = record.work_for_hire

        encoded['writer'] = self.encode(record.writer)

        return encoded

    def __encode_iswc(self, iswc):
        """
        Creates a dictionary from a ISWCCode.

        :param iswc: the ISWCCode to transform into a dictionary
        :return: a dictionary created from the ISWCCode
        """
        encoded = {}

        encoded['id_code'] = iswc.id_code
        encoded['check_digit'] = iswc.check_digit

        return encoded

    def __encode_ipi_base(self, ipi):
        """
        Creates a dictionary from a IPIBaseNumber.

        :param ipi: the IPIBaseNumber to transform into a dictionary
        :return: a dictionary created from the IPIBaseNumber
        """
        encoded = {}

        encoded['header'] = ipi.header
        encoded['id_code'] = ipi.id_code
        encoded['check_digit'] = ipi.check_digit

        return encoded

    def __encode_visan(self, visan):
        """
        Creates a dictionary from a VISAN.

        :param visan: the VISAN to transform into a dictionary
        :return: a dictionary created from the VISAN
        """
        encoded = {}

        encoded['version'] = visan.version
        encoded['isan'] = visan.isan
        encoded['episode'] = visan.episode
        encoded['check_digit'] = visan.check_digit

        return encoded

    def __encode_avi_key(self, avi_key):
        """
        Creates a dictionary from a AVIKey.

        :param avi_key: the AVIKey to transform into a dictionary
        :return: a dictionary created from the AVIKey
        """
        encoded = {}

        encoded['society_code'] = avi_key.society_code
        encoded['av_number'] = avi_key.av_number

        return encoded

    def __encode_table_value(self, value):
        """
        Creates a dictionary from a TableValue.

        :param value: the TableValue to transform into a dictionary
        :return: a dictionary created from the TableValue
        """
        encoded = {}

        encoded['code'] = value.code
        encoded['name'] = value.name
        encoded['description'] = value.description

        return encoded

    def __encode_media_type_value(self, value):
        """
        Creates a dictionary from a MediaTypeValue.

        :param value: the MediaTypeValue to transform into a dictionary
        :return: a dictionary created from the MediaTypeValue
        """
        encoded = {}

        encoded['code'] = value.code
        encoded['name'] = value.name
        encoded['media_type'] = value.media_type
        encoded['duration_max'] = value.duration_max
        encoded['works_max'] = value.works_max
        encoded['fragments_max'] = value.fragments_max

        return encoded

    def __encode_instrument_value(self, value):
        """
        Creates a dictionary from a InstrumentValue.

        :param value: the InstrumentValue to transform into a dictionary
        :return: a dictionary created from the InstrumentValue
        """
        encoded = self.__encode_table_value(value)

        encoded['family'] = value.family

        return encoded

    def __encode_file_tag(self, value):
        """
        Creates a dictionary from a TableValue.

        :param value: the TableValue to transform into a dictionary
        :return: a dictionary created from the TableValue
        """
        encoded = {}

        encoded['year'] = value.year
        encoded['sequence_n'] = value.sequence_n
        encoded['sender'] = value.sender
        encoded['receiver'] = value.receiver
        encoded['version'] = value.version

        return encoded

    def __encode_file(self, value):
        """
        Creates a dictionary from a TableValue.

        :param value: the TableValue to transform into a dictionary
        :return: a dictionary created from the TableValue
        """
        encoded = {}

        encoded['tag'] = self.encode(value.tag)
        encoded['transmission'] = self.encode(value.transmission)

        return encoded
