
import logging
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from sentence_transformers import SentenceTransformer

class MixtralModel():

    def __init__(self):
        logging.warning("Loading Mixtral model. May take time.")

        self.tokenizer = AutoTokenizer.from_pretrained("mistralai/Mixtral-8x7B-Instruct-v0.1")

        self.model = AutoModelForCausalLM.from_pretrained("mistralai/Mixtral-8x7B-Instruct-v0.1",
                                                          torch_dtype=torch.float16,
#                                                          attn_implementation="flash_attention_2",
                                                          device_map="auto")
        logging.warning("Model ready.")

    def answer(self, prompt):

        messages = [{"role": "user", "content": prompt}]
        chat_in = self.tokenizer.apply_chat_template(messages, return_tensors="pt").to("cuda")
        generated_ids = self.model.generate(
            chat_in,
            pad_token_id=self.tokenizer.eos_token_id,
            max_new_tokens=100,
            do_sample=True
        )
        out = self.tokenizer.batch_decode(generated_ids)[0]
                                                                                  
        return out 


class Embedding():

    def __init__(self):
        logging.warning("Loading Sentence Transformer.")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        logging.warning("Sentence Transformer Ready.")
        

    def encode(self, sentences):
        return self.model.encode(sentences)
