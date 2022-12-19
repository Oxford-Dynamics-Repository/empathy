# Johann Diep (johann@oxdynamics.com) - Oxford Dynamics - December 2022
#
# This script does inference with the trained language models. 

from transformers import pipeline


# Running inference using the pipeline abstraction.
def get_inference(model, tokenizer, prompt):
    generator = pipeline(task = 'text-generation', 
        model = model, 
        tokenizer = tokenizer, 
        max_new_tokens = 100,
        pad_token_id = 50256)
    print(generator(prompt))

def main():    
    # Defining the prompt
    prompt = 'You can eat ice cream in Paris and '
    
    get_inference('distilgpt2-finetuned/checkpoint-14500', 'distilgpt2', prompt)
    get_inference('distilgpt2', 'distilgpt2', prompt)


if __name__ == '__main__':
    main()