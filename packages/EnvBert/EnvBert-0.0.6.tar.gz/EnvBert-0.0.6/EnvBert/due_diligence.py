# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 17:00:39 2022

@author: EL221XK
"""

#Loading Packages
import numpy as np
import transformers
import sklearn
import sentence_transformers
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity
similarity_model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')

#%% 
#Classification Model
tokenizer = AutoTokenizer.from_pretrained("d4data/environmental-due-diligence-model")
model = TFAutoModelForSequenceClassification.from_pretrained("d4data/environmental-due-diligence-model")
classifier = pipeline('text-classification', model=model, tokenizer=tokenizer) # cuda = 0,1 based on gpu availability

#%%
def predict(text_input):
    #running the classification model to predict the classes
    edd_classification = classifier(text_input)
    edd_label = edd_classification[0]['label']
    edd_score = edd_classification[0]['score']
    
    #running due diligence ranking module
    # due diligence ranking dictionary

    remediation_activities = ['existing remedy ', 'selected remedy', 'remedy consists of', 'active remediation', 'remedies-in-place', 'remedy was completed', 'remedy components', 'in situ treatment', 'insitu treatment', 'expanded remedy', 'remedial systems', 'chemically treat', 'recovery and treatment system', 'Monitoring for natural attenuation', 'MNA', 'Monitored Natural Attenuation with Land Use Controls', 'bioremediation', 'biodegradation, outgassing, dispersion, and dilution', 'natural attenuation, dispersion, and dilution', 'soil excavation', 'Carbon substrate injection', 'injection ', 'carbon substrate injection, recirculation, and infiltration', 'substrate injection and bioaugmentation activities', 'injected to biologically degrade', 'In Situ Chemical Oxidation (ISCO) ', 'Physical, chemical, or biological measures applied', 'Limited excavation', 'site remediation', 'will be installed', 'BioTrap Installation', 'Injection Well Installation', 'demolished', 'achieve site closure', 'land use control', 'lucs remedy', 'Institutional control', 'Interim RA activities', 'Disposal of contaminated soil ', 'Phytoremediation, Free Product Recovery', 'Installation of pumps, piping, bioreactor and treatment equipment', 'extraction and treatment system', 'abandonment of monitoring wells', 'dewatering trench and treatment system construction', 'remedy has been implemented across', 'Remedial alternatives', 'reductive dechlorination', 'alternatives evaluated', 'Alternative No.', 'decomposition stage that the landfill is in', 'remedial approach', 'barriers were added', 'evaluate remedial options', 'Treatment alternatives were evaluated', 'Installation of wells', 'Subgrade Biogeochemical Reactor', 'Enhanced Reductive Dechlorination Biobarriers', 'low-permeability cap has been installed', 'No Action', 'Full-scale Enhanced Reductive Dechlorination Bioremediation Well Design', 'extraction wells were planned', 'volatilization', 'enhanced reductive dechlorination (ERD)']
    
    gw_sw_interaction = ['water discharges', 'rainwater precipitation', 'water moves', 'water enters', 'water exits', 'water recharge', 'water movement', 'water reaches', 'water join seepage flow', 'water flow', 'water overflows', 'water migrates', 'water travels', 'water runoff', 'water exchange', 'discharge to water', 'water infiltrates', 'water interacts']
    
    contaminants = ['contaminants', 'primary contaminant', 'co-contaminant', 'lnapl', 'dnapl', 'coc', 'copec', 'compounds', 'chemicals', 'primary chemicals', 'analyzed', 'sampled', 'detected', 'constituents detected', 'concentrations exceeded', 'analyte', 'products', 'contamination', 'detected above', 'elevated concentrations', 'concentration', 'maximum detected concentration']
    
    contamination_extent = ['nature and extent of contamination', 'exceed regulatory screening levels', 'horizontal and vertical distribution of COPCs', 'concentrations', 'exceedances', 'contaminant released', 'contaminants transported', 'contaminants deposited', 'contaminants leaching', 'not detected in nearby samples', 'impacts are limited to the area', 'plume extending', 'plume discharges ', 'chemical transport pathways', 'delineation', 'exposure pathways', 'originating from contaminated', 'contaminants migrated ', 'contamination is travelling', 'widespread contaminant', 'plumes length ranging from', 'Plume widths range from ', 'extent of contamination', 'plumes migrate', 'contraction of the plumes', 'plume expansion', 'plume stable', 'plume contracting', 'area of impact', 'lateral and vertical extent in groundwater']
    
    contaminated_media = ['soil contamination', 'groundwater contamination', 'contaminated media ', 'contaminated sediments', 'contaminated air', 'impacted areas', 'groudwater samples', 'soil samples']
    
    source = ['source', 'historical', 'prior', 'originates', 'release', 'result of', 'likely', 'reportedly occurred', 'emanating ', 'past use']
    
    depth = ['depth', 'feet', 'feet below grade', 'feet mean sea level', 'msl', 'depth to water', 'feet below ground surface', 'bgs', 'water table', 'Static water levels']
      
    velocity = ['velocity', 'ft/sec', 'feet per minute', 'hydraulic', 'transmissivities ', 'slug']
    
    standards = ['above mcl', 'above maximum contaminant levels', 'below mcl', 'below maximum contaminant levels', 'achieve mcls', 'meet mcl', 'exceeding mcls', 'proposed mcls', 'mcl', 'mcls', 'above srg', 'above gctl', 'exceeded mcls', 'exceedances of maximum contaminant levels', 'exceed rbsls', 'greater than the residential rbsl', 'above rbsl', 'maximum rbsl', 'rbsls were used', 'adjusted from the Oak Ridge National Laboratory to Regional Screening Levels', 'lower than srgs', 'To-Be-Considered (TBC) criteria were used', 'meeting MDE Standards', 'SRGs established', 'over the MCL standard', 'MCLs are achieved', 'MCLs where available', 'compared to respective federal MCLs or USEPA Region III RBCs', 'absence of specified cleanup levels or MCLs', 'attainment of UTLs', 'higher than TBC', 'achieve srgs', 'less than cbsgs ', 'above cbsg', 'below prg', 'exceeded sctl', 'swctl used', 'rsl was used', 'pal exceeded', 'meeting ctl', 'Cleanup Target', 'Screening Level', 'Project Action Limit', 'below', 'above', 'clean up criteria', 'exceed', 'criteria', 'Goal']
    
    goals = ['Site closure', 'closure goals', 'remedial action objectives', 'RAOs', 'continue remove LNAPL', 'Continue LNAPL', 'Continue assess', 'achieve cleanup level', 'land use control', 'meet', 'LUC', 'current future use', 'monitored inspected annually', 'no further action required', 'response action', 'recommended', 'evaluate progress', 'evaluate compliance', 'Corrective actions', 'follow-up']
    
    geology = ['geology', 'topography', 'lithology', 'physiography', 'cross sections', 'stratigraphy', 'silt sediment gravel deposits rock']

    embeddings_text = similarity_model.encode([text_input])
    if edd_label == 'Remediation Standards':
        embeddings_dict = similarity_model.encode([" ".join(standards)])
    
    if edd_label == 'Extent of contamination':
        embeddings_dict = similarity_model.encode([" ".join(contamination_extent)])   
    
    if edd_label == 'Depth to Water':
        embeddings_dict = similarity_model.encode([" ".join(depth)])   
        
    if edd_label == 'Groundwater-Surfacewater interaction':
        embeddings_dict = similarity_model.encode([" ".join(gw_sw_interaction)])   
        
    if edd_label == 'GW Velocity':
        embeddings_dict = similarity_model.encode([" ".join(velocity)])   
        
    if edd_label == 'Geology':
        embeddings_dict = similarity_model.encode([" ".join(geology)])
        
    if edd_label == 'Contaminated media':
        embeddings_dict = similarity_model.encode([" ".join(contaminated_media)])   
        
    if edd_label == 'Source of contamination':
        embeddings_dict = similarity_model.encode([" ".join(source)])   
           
    if edd_label == 'Remediation Activities':
        embeddings_dict = similarity_model.encode([" ".join(remediation_activities)])   
    
    if edd_label == 'Remediation Goals':
        embeddings_dict = similarity_model.encode([" ".join(goals)])  
        
    if edd_label == 'Contaminants':
        embeddings_dict = similarity_model.encode([" ".join(contaminants)])
    
                                        
    cosine_scores = util.cos_sim(embeddings_text, embeddings_dict)
    
    final_probability = np.float64(cosine_scores)
    
    if final_probability > 0.3:
        return [edd_label, np.float64(cosine_scores)]
    else:
        return ["Not Relevant", np.float64(cosine_scores)]

#%%

