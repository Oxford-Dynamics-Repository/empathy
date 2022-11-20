# Lucy Jackson (lucy@oxdynamics.com) - Oxford Dynamics - November 2022
#
# This script is for testing the GODEL model.

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from converse_t2s_s2t import speech_to_text, text_to_speech


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
    # Defining the instruction.
    instruction = f'Instruction: given a dialog context and related knowledge, you need to response safely based on the knowledge.'

    knowledge_input = input('Knowledge: ')
    question_input = speech_to_text()
    print("Question: " + question_input)

    knowledge = f'{knowledge_input}'
    dialog = [f'{question_input}']

    response = generate(instruction, knowledge, dialog)
    print("Response: " + response)
    text_to_speech(response)

    dialog.append(response)

    while question_input != '':
        knowledge_input = input('Knowledge: ')
        question_input = speech_to_text()
        print("Question: " + question_input)

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