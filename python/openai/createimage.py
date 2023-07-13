#Get the list of models available in open AI
import os
import openai

# This the file got created a a global environment file , where you have to set the API key and org key for your account
import openaienv
openai.organization = openaienv.GLOBAL_ORG_KEY
openai.api_key = openaienv.GLOBAL_API_KEY
# use the link https://openai.com/research/dall-e to try different prompts to generate different images
response = openai.Image.create(
  prompt="a loft bedroom with a white bed white bed next to a nightstand nightstand. there is a fish tank fish tank standing beside the bed.",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print (image_url)