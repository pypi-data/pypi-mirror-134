import pandas as pd
import pandas_plink
from pandas_plink import read_plink1_bin
genetic_data_location="/ocean/projects/asc170022p/tighu/UKB_Genetic_Data"
class genetic_data_handler:

    """
    A class to represent family of methods that can fetch pandas object based on subject id

    ...

    Attributes
    ----------
    number_of_subjects : int
        number of subjects to fetch genetic data for

    chromosome_number_list: list of strings
        list of chromosomes that need to retrived

    subject_id : string
        subject_id whose genetic data need to fetched

    Methods
    -------


    get_genetic_data_single_subject(subject_id,chromosome_number_list):
        retrieves pandas object for the particular subject having genetic data of the specified chromosomes

    get_genetic_data_batch(number_of_subjects,chromosome_number_list):
        get pandas object having genetic data corresponding to the specified chromosome for specified number of subjects

    """

    def __init__(self, chromosome_number_list=None, number_of_subjects=1):
        if chromosome_number_list is None:
            chromosome_number_list = ["A"]
        self.chromosome_number_list = chromosome_number_list
        self.number_of_subjects = number_of_subjects




    def get_genetic_data_single_subject(self,subject_id):

        """
        A utility function which lets user fetch the genetic data associated with a particular subject_id

        Parameters:
        a string representing a subject and list of chromosomes of interest

        Returns:
        categories list: pandas object having genetic data of that particular subject
        :rtype: pandas table
        """
        path_to_bed_file = ""
        genetic_data_object = pandas_plink.Chunk()

        for chr_num in self.chromosome_number_list:
            path_to_bed_file = chr_num+".bed"
            tmp_plink_object = read_plink1_bin(path_to_bed_file)
            genetic_data_object.append(tmp_plink_object[tmp_plink_object['subject_id'] == subject_id])


        return genetic_data_object

    def get_genetic_data_batch(self,number_of_subjects=10):
        """
        A utility function which lets user fetch the genetic data related to chromosomes mentioned and for a fixed number of subjects

        Parameters:
        number of subjects and chromosome list

        Returns:
        genetic_data_object: a pandas object which contains the genetic info for
        :rtype: pandas table
        """

        genetic_data_object = pandas_plink.Chunk()


        # for chr_num in self.chromosome_number_list:
        #     path_to_bed_file = chr_num+".bed"
        #     tmp_plink_object = read_plink1_bin(path_to_bed_file)
        #     genetic_data_object.append(tmp_plink_object.head(number_of_subjects))

        return genetic_data_object