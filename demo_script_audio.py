# Stefan Karmakov (stefan@oxdynamics.com) - Oxford Dynamics - November 2022
#
# Main script for convAI demo
#!/usr/bin/env python3
import os

from parlai.scripts.interactive import Interactive
from parlai.core.message import Message

from empathy.intermediate_scripts.hold_conversation import HoldConversation
from empathy.scripts.converse_t2s_s2t import VoiceClass
# from empathy.scripts.visualizer import PrintOutputs

def create_chat_files(user_input, avis_output, base_path):
    path_user = base_path + '/' + 'user.txt'
    path_avis = base_path + '/' + 'avis.txt'

    with open(path_user, 'a') as pu:
        pu.write(user_input + '\n')

    with open(path_avis, 'a') as pa:
        pa.write(avis_output + '\n')

def main():
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    agent, world = Interactive.main(model_file='zoo:seeker/seeker_dialogue_400M/model', init_opt='gen/seeker_dialogue', search_server='0.0.0.0:8080')
    _, _, dra = agent.get_seeker_modules()

    voice_obj = VoiceClass()
    tapas_obj = HoldConversation()
    # visualizer_obj = PrintOutputs()
    # print(visualizer_obj)

    tmp_text_path = '/home/lucy/military_demo/tmp_text'
    fpu = open(tmp_text_path + '/user.txt', 'w').close()
    fpa = open(tmp_text_path + '/avis.txt', 'w').close()

    while True:
        human_input = voice_obj.speech_to_text()
        if human_input.lower()=='cancel':
            break
        # human_input = input("Human: ")
        # TAPAS
        # visualizer_obj.print_user(fpu)

        tapas_knowledge_output = tapas_obj.generate_seeker_input(human_input)
        temp_history_template = f"\n__knowledge__ {tapas_knowledge_output} __endknowledge__"

        # Seeker
        drm_obs = {'id': 'localHuman',
                    'episode_done': False,
                    'text': human_input,
                    'knowledge_response': '',
                    'temp_history': temp_history_template,
                    'skip_retrieval': True}

        # print('======== drm_obs ========')
        # print(drm_obs)

        drm_obs = Message(drm_obs)
        dialogue_agent_observations = [dra.observe(drm_obs)]

        # print('======== dialogue_agent_observations ========')
        # print(dialogue_agent_observations)
        # print('333333') 
        # print(dra.history.get_history_str())

        response = dra.batch_act(dialogue_agent_observations)
        text_response = response[0]['text']
        # visualizer_obj.print_avis(fpa)

        print('AVIS: ' + text_response)
        # voice_obj.text_to_speech(text_response)
        os.system("say " + text_response.replace("'",""))

        dra.history.add_reply(text_response)
        full_text_hist = dra.history.get_history_str()
        conv = 3
        all_conv_num = conv*2 + 1
        if full_text_hist.count('\n') > all_conv_num:
            split_text = full_text_hist.split('\n')
            num_to_del = len(split_text) - all_conv_num
            new_text = '\n'.join(split_text[num_to_del:-1])
            dra.history.reset()
            dra.history.add_reply(new_text)

        # print('444444') 
        # print(dra.history.get_history_str())
        create_chat_files(human_input, text_response, tmp_text_path)


if __name__ == "__main__":
    main()
