# Lucy Jackson (lucy@oxdynamics.com) - Oxford Dynamics - November 2022
#
# This script is for testing the GODEL model.

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import TapasTokenizer, TapasForQuestionAnswering
# from converse_t2s_s2t import speech_to_text, text_to_speech
from get_keywords import get_keywords
from return_database import return_database

def generate(output, coordinate, table):
    # tokenizer = AutoTokenizer.from_pretrained("microsoft/GODEL-v1_1-base-seq2seq")
    # model = AutoModelForSeq2SeqLM.from_pretrained("/home/lucy/Documents/IRIS/Code/GODEL/GODEL/results_new/checkpoint-600")
    if table.iloc[coordinate[0][0][0],:][0] != "":
        outter = table.iloc[coordinate[0][0][0],:][0]
    elif table.iloc[coordinate[0][0][0],:][6] != "":
        outter = table.iloc[coordinate[0][0][0],:][6]
    else:
        outter = table.iloc[coordinate[0][0][0],:][7]
    # if knowledge != '':
    #     knowledge = '[KNOWLEDGE] ' + knowledge
    # dialog = ' EOS '.join(dialog)
    # query = f"{instruction} [CONTEXT] {dialog} {knowledge}"
    # input_ids = tokenizer(f"{query}", return_tensors="pt").input_ids
    # outputs = model.generate(input_ids, max_length=128, min_length=8, top_p=0.8, do_sample=False)
    # output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    if coordinate[0][0][1] == 0:
        response = f'There are {output} around.'
    if coordinate[0][0][1] == 1:
        response = f'The {outter} are {output} away'
    if coordinate[0][0][1] == 2:
        response = f'The {outter} are armed with {output}'
    if coordinate[0][0][1] == 3:
        response = f'The {outter} are on {output}'
    if coordinate[0][0][1] == 4:
        response = f'The {outter} are wearing {output}.'
    if coordinate[0][0][1] == 5:
        response = f'The {outter } is {output}.'
    if coordinate[0][0][1] == 6:
        response = f'There are {output} around.'    
    if coordinate[0][0][1] == 7:
        response = f'There are {output} around.'    
    return response


def hold_conversation():
    # Initialising the model used to extract the knowledge from a question.
    tapas = "google/tapas-base-finetuned-wtq"
    tapas_model = TapasForQuestionAnswering.from_pretrained(tapas)
    tapas_tokenizer = TapasTokenizer.from_pretrained(tapas)

    table = return_database()
    print(table)
    # Defining the instruction.
    instruction = f'Instruction: given a dialog context and related knowledge, you need to response safely based on the knowledge.'

    print(">> I am listening.")
    # question_input = speech_to_text()
    question_input = input('How can I help?')
    print("Question: " + question_input)

    knowledge_input, coordinates = get_keywords(question_input, tapas_model, tapas_tokenizer, table)
    print("Extracted Knowledge: " + knowledge_input)
    knowledge = f'{knowledge_input}'
    dialog = [f'{question_input}']

    response = generate(knowledge_input, coordinates, table)
    print("Response: " + response)
    # text_to_speech(response)
    # dialog.append(response)

    while question_input != '':
        print(">> I am listening.")
        question_input = input('How can I help?')
        # question_input = speech_to_text()
        print("Question: " + question_input)
        if(question_input == 'cancel'): break


        knowledge_input, coordinates = get_keywords(question_input, tapas_model, tapas_tokenizer, table)
        print("Extracted Knowledge: " + knowledge_input)
        knowledge = f'{knowledge_input}'
        # dialog.append(question_input)

        response = generate(knowledge_input, coordinates, table)
        print("Response: " + response)
        # text_to_speech(response)
        # dialog.append(response)

def main():
    hold_conversation()
    

if __name__ == '__main__':
    main()