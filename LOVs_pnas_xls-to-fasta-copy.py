######################################

#To run in Python, please save this text file as the ".py" file type, which can be run with the Python language. Make sure that Dataset_S4 is saved in the same folder as your .py python file.

######################################
#USER INPUT PARAMETERS

#Enter the filename you have chosen for the Dataset_S4 spreadsheet

inFile = 'LOV_pnas.xls'  #
outputFile = open('LOVS.fasta', 'w')   #ANNA
#Enter desired protein parameters. Leave 'none' for each if no preference. Surround each entry with a single quote ('entry') other than for functional_cluster_set, which requires double quotes ("[]")

primary_sequence_set = 'none' #Enter arbitrary single letter amino acid sequence, i.e. 'MAGTD'
kingdom_set = 'Bacteria' #Choose between 'Land Plants', 'Protist', 'Bacteria', 'Archaea', 'Fungi')
phylum_set = 'none' #Enter a phylum of interest relevant to the selected kingdom
primary_effector_set = 'none' #Chose a primary_effector "short_name" listed in Supplementary_Table_2
primary_effector_ontology = 'none' #Chose a primary_effector ontology listed in Figure_3
functional_cluster_set = "none" #Enter in format ['Domain1', 'Domain2', 'Domain3'] with Domains in alphabetical order (with domain "short_names" from Supplementary Table 2)
photoadduct_motif_set = 'none' #Enter in format GXNCRFLQ
linker_length_range = '-1,1000' #Chose an desired range for the linker lengths in the format: minimum_length,maximum_length, ex: '0,100'

parameter_set = [kingdom_set, phylum_set,primary_effector_set,primary_effector_ontology,functional_cluster_set, primary_sequence_set, photoadduct_motif_set, linker_length_range]

#Enter desired output - choose between print to screen (yes or no) and print to excel

print_to_screen = 'no' #Do you want results to print to the screen?
print_to_excel = 'yes' #Do you want results to print to Excel?
excel_file_name = 'Bacteria_LOV.xls' #Enter name of desired output file

##################################################
#PROGRAM EXECUTION (Please do not edit below)

import xlrd
import xlwt

def Row_process(i):
    sequence = str(Data_table.cell(i,3).value)
    kingdom = str(Data_table.cell(i,13).value)
    phylum = str(Data_table.cell(i,14).value)
    primary_effector = str(Data_table.cell(i,8).value)
    primary_effector_ontology = str(Data_table.cell(i,9).value)
    Linker_length = str(Data_table.cell(i,10).value)
    functional_cluster = str(Data_table.cell(i,7).value)
    photoadduct_motif = str(Data_table.cell(i,4).value)
    return   [kingdom, phylum, primary_effector,primary_effector_ontology,functional_cluster, sequence, photoadduct_motif,Linker_length]

def outfile_generate():
    wbnew = xlwt.Workbook()
    ws = wbnew.add_sheet('Datatable',cell_overwrite_ok=True)
    ws.write(0,0,'Database Source')
    ws.write(0,1,'Sequence ID')
    ws.write(0,2,'GenBank ID')
    ws.write(0,3,'Primary Structure')
    ws.write(0,4,'GXNCRFLQ Motif')
    ws.write(0,5,'Protein Length')
    ws.write(0,6,'Domain Structure')
    ws.write(0,7,'Functional Cluster')
    ws.write(0,8,'Primary Effector')
    ws.write(0,9,'Primary Effector Gene Ontology')
    ws.write(0,10,'Linker Length')
    ws.write(0,11,'Number of Predicted Transmembrane Helices')
    ws.write(0,12,'Transmembrane Helix Topology ')    
    ws.write(0,13,'Kingdom')
    ws.write(0,14,'Phylum')
    ws.write(0,15,'Class')
    ws.write(0,16,'Family')
    ws.write(0,17,'Order')
    ws.write(0,18,'Genus')
    ws.write(0,19,'Species')
    return ws,wbnew

def excel_print(i,excel_file_name,ws,wbnew,outputFile):
    Database_source  = str(Data_table.cell(i,0).value)
    ID = str(Data_table.cell(i,1).value)
    GenBank_ID = str(Data_table.cell(i,2).value)
    primary_structure = str(Data_table.cell(i,3).value)
    photoadduct_motif = str(Data_table.cell(i,4).value)
    Protein_length = str(Data_table.cell(i,5).value)
    Domain_structure = str(Data_table.cell(i,6).value)
    functional_cluster = str(Data_table.cell(i,7).value)
    primary_effector = str(Data_table.cell(i,8).value)
    primary_effector_ontology = str(Data_table.cell(i,9).value)
    Linker_length = str(Data_table.cell(i,10).value)
    Num_TMH = str(Data_table.cell(i,11).value)
    Arrangement_TMH = str(Data_table.cell(i,12).value)
    kingdom = str(Data_table.cell(i,13).value)
    phylum = str(Data_table.cell(i,14).value)
    class_taxon = str(Data_table.cell(i,15).value)
    family = str(Data_table.cell(i,16).value)
    order = str(Data_table.cell(i,17).value)
    genus = str(Data_table.cell(i,18).value)
    species = str(Data_table.cell(i,19).value)
    ws.write(c,0,str(Database_source))
    ws.write(c,1,str(ID))
    outputFile.write(">" + str(ID) + "\n")   #ANNA
    ws.write(c,2,str(GenBank_ID))
    ws.write(c,3,str(primary_structure))
    outputFile.write(str(primary_structure) + "\n")  #ANNA
    ws.write(c,4,str(photoadduct_motif))
    ws.write(c,5,str(Protein_length))
    ws.write(c,6,str(Domain_structure))
    ws.write(c,7,str(functional_cluster))
    ws.write(c,8,str(primary_effector))
    ws.write(c,9,str(primary_effector_ontology))
    ws.write(c,10,str(Linker_length))
    ws.write(c,11,str(Num_TMH))
    ws.write(c,12,str(Arrangement_TMH))
    ws.write(c,13,kingdom)
    ws.write(c,14,phylum)
    ws.write(c,15,class_taxon)
    ws.write(c,16,family)
    ws.write(c,17,order)
    ws.write(c,18,genus)
    ws.write(c,19,species)
    wbnew.save(excel_file_name)

c = 1
wb = xlrd.open_workbook(inFile)
Data_table = wb.sheet_by_index(0)
if print_to_excel == 'yes':
    ws,wbnew = outfile_generate()
    wbnew.save(excel_file_name)

for i in range(4,(Data_table.nrows)):
    parameter_value = Row_process(i)
    for n in range(0,6):
        if parameter_set[n] != 'none' and parameter_set[n] not in parameter_value[n]:
            Selected = False
            break
        else:
            Selected = True

    if Selected == True:
        n = 7
        if parameter_set[n] != 'none':
            length_range = parameter_set[n]
            length_range_start = length_range.split(',')[0]
            length_range_end = length_range.split(',')[1]
            if float(parameter_value[n]) > float(length_range_start) and float(parameter_value[n]) < float(length_range_end):
                Selected = True
            else:
                Selected = False
            
    if Selected == True and print_to_screen == 'yes':
        ID = str(Data_table.cell(i,1).value)
        Domain_structure = str(Data_table.cell(i,6).value)
        print ('ID: ' + ID + ' *  Domain-structure: ' + Domain_structure + ' *  Kingdom: ' + str(parameter_value[1]) + ' * Phylum: ' + str(parameter_value[2]) + ' * Sequence: ' + str(parameter_value[0]))
    if Selected == True and print_to_excel == 'yes':
        excel_print(i,excel_file_name,ws,wbnew,outputFile)
        c+=1

print ('done')

    
    
    
    
    
    
