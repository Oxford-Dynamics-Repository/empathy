# Lucy Jackson (lucy@oxdynamics.com) - Oxford Dynamics - November 2022
#
# This script is for testing the GODEL model.

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import TapasTokenizer, TapasForQuestionAnswering
from converse_t2s_s2t import speech_to_text, text_to_speech
from get_keywords import get_keywords


def generate(instruction, knowledge, dialog):
    tokenizer = AutoTokenizer.from_pretrained("microsoft/GODEL-v1_1-base-seq2seq")
    model = AutoModelForSeq2SeqLM.from_pretrained("microsoft/GODEL-v1_1-base-seq2seq")

    if knowledge != '':
        knowledge = '[KNOWLEDGE] ' + knowledge
    dialog = ' EOS '.join(dialog)
    query = f"{instruction} [CONTEXT] {dialog} {knowledge}"
    input_ids = tokenizer(f"{query}", return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=128, min_length=8, top_p=0.8, do_sample=False)
    output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return output


def hold_conversation():
    # Initialising the model used to extract the knowledge from a question.
    tapas = "google/tapas-base-finetuned-wtq"
    tapas_model = TapasForQuestionAnswering.from_pretrained(tapas)
    tapas_tokenizer = TapasTokenizer.from_pretrained(tapas)

    # Defining the instruction.
    instruction = f'Instruction: given a dialog context and related knowledge, you need to response safely based on the knowledge.'

    print(">> I am listening.")
    question_input = speech_to_text()
    print("Question: " + question_input)

    knowledge_input = get_keywords(question_input, tapas_model, tapas_tokenizer)
    print("Extracted Knowledge: " + knowledge_input)
    knowledge = f'{knowledge_input}'
    dialog = [f'{question_input}']

    response = generate(instruction, knowledge, dialog)
    print("Response: " + response)
    text_to_speech(response)
    dialog.append(response)

    while question_input != '':
        print(">> I am listening.")
        question_input = speech_to_text()
        print("Question: " + question_input)
        if(question_input == 'cancel'): break


        knowledge_input = get_keywords(question_input, tapas_model, tapas_tokenizer)
        print("Extracted Knowledge: " + knowledge_input)
        knowledge = f'{knowledge_input}'
        dialog.append(question_input)

        response = generate(instruction, knowledge, dialog)
        print("Response: " + response)
        text_to_speech(response)
        dialog.append(response)

def main():
    hold_conversation()
    

if __name__ == '__main__':
    main()