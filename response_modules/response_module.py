from sentence_understanding import naive_bayes_model
from response_modules import casual_responses

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def process_message(message):
    """
    This function process the information received from chat and returns a response
    :param message: Contains the message
    :return: string with the appropriate response
    """
    # TODO: Move this to settings
    lower = 0.7

    #########################---Model Loading Phase----##############################
    # In this phase a machine learning model is loaded and the model makes the prediction
    # If model did not exists, the model needs to be trained and then make the
    # prediction, this phase returns a label with the command type

    skill_label, prob_type = naive_bayes_model.predict_label(message)

    logger.debug("SKILL LABEL: %s", skill_label)

    if prob_type < lower:
        skill_label = 'unknown'

    #########################------Response Phase------##############################
    # In this phase a response is returned based on model prediction, the response
    # will be a string

    # Get response String array
    # TODO: Check this
    response = get_response_from_message(skill_label,message)

    return response


def get_response_from_message(skill_label,mensaje):
    """
    Base on skill_label this method generate the info that the user needs
    :param skill_label: skill used for the response
    :return: String with the info required
    """
    if __name__ == '__main__':
        stopwords = ['porfavor','la','del']

        sentence =["porvafor la cancion del noa noa"]

    temp = []
    for sentence in sentences:

        tokens = sentence.split(" ")
        clean_tokens = []

        for token in tokens:
            if all(char in set(string.punctuation) for char in token):
                continue

            if token.isdigit():
                continue

            token = token.lower()
            token = token.strip()

            if token in stopwords:
                continue
        
            clean_tokens.append(token)

        temp.append(' '.join(clean_tokens))


    #bag of words transformation
    count_vect = CountVectorizer()
    bag_of_words_array = count_vect.fit_transform(temp)

    #model training
    naive_bayes_classifier = MultinomialNB()
    naive_bayes_classifier.fit(bag_of_words_array,['juanes','clima','nombre'])

    
    hola= "cual es el clima"
    hola2 = []

    tokens = hola.split(" ")

    #sentecne cleaning
    hola1 = []

    for token in tokens:
        if all(char in set(string.punctuation) for char in token):
            continue

        if token.isdigit():
            continue

        token = token.lower()
        token = token.strip()

        if token in stopwords:
            continue
    
        hola1.append(token)



    # only for this practice

    hola2.append(' '.join(hola1))
    

    #bag of words transformation
    count_vect2 = CountVectorizer()
    bag_of_words_array2 = count_vect.transform(hola2)




    #model predict
    print("predict...")
    print(naive_bayes_classifier.predict(bag_of_words_array2))

    """
    Implementar 3 oraciones 

    """






    logger.debug("SKILL LABEL: %s", skill_label)


    try:
        if skill_label == 'unknown':
            skill_label = 'definitions' #google

        # import module dynamically
        # TODO move this to configuration file
        module_name = "response_modules.%s" % skill_label
        skill_module = __import__(module_name, fromlist=[''])


 #if skill label == 'musica' or skill label =='google':
	   #response= skill_module.get_response(word) 	
	   #else:
	   #response= skill_module.get_response() 

  
     

	


	

    except ImportError:
        logger.warning("IMPOSSIBLE TO IMPORT MODULE DEFAULT BEHAVIOR USED")
        response = casual_responses.get_not_understand()

    return response
