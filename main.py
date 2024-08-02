{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "b20dccbf-3893-46db-a16b-fe98b0e4e461",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'langchain_openai'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[22], line 12\u001b[0m\n\u001b[0;32m      3\u001b[0m os\u001b[38;5;241m.\u001b[39menviron[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mOPENAI_AI_KEY\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124msk-proj-08NdvjzdGcV_0AYsaLIjjSiVGlAYN74bPdHZ-SNXlA8sRbQoCbywdobRjMT3BlbkFJDgUD_hiW1aIp2cOyRE_zM1OkcsRH9qabZ56yPVHdzM_DdFetBckYXGHG4A\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[0;32m      5\u001b[0m \u001b[38;5;66;03m#form langchail.llms import OpenAI\u001b[39;00m\n\u001b[0;32m      6\u001b[0m \u001b[38;5;66;03m#llm = OpenAI()\u001b[39;00m\n\u001b[0;32m      7\u001b[0m \n\u001b[0;32m      8\u001b[0m \u001b[38;5;66;03m#content = \"코딩\"\u001b[39;00m\n\u001b[0;32m      9\u001b[0m \u001b[38;5;66;03m#result = llm.predict(content + \"에 대한 시를 써줘\")\u001b[39;00m\n\u001b[0;32m     10\u001b[0m \u001b[38;5;66;03m#print(result)\u001b[39;00m\n\u001b[1;32m---> 12\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mlangchain_openai\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m ChatOpenAI\n\u001b[0;32m     14\u001b[0m chatgpt \u001b[38;5;241m=\u001b[39m  ChatOpenAI()\n\u001b[0;32m     15\u001b[0m chatgpt \u001b[38;5;241m=\u001b[39m ChatOpenAI(model_name\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mgpt-3.5-turbo\u001b[39m\u001b[38;5;124m\"\u001b[39m, max_tokens \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m512\u001b[39m)\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'langchain_openai'"
     ]
    }
   ],
   "source": [
    "#import os\n",
    "\n",
    "#os.environ[\"OPENAI_AI_KEY\"] = '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'\n",
    "\n",
    "#form langchail.llms import OpenAI\n",
    "#llm = OpenAI()\n",
    "\n",
    "#content = \"코딩\"\n",
    "#result = llm.predict(content + \"에 대한 시를 써줘\")\n",
    "#print(result)\n",
    "\n",
    "from langchain_openai import ChatOpenAI\n",
    "\n",
    "chatgpt =  ChatOpenAI()\n",
    "chatgpt = ChatOpenAI(model_name=\"gpt-3.5-turbo\", max_tokens = 512)\n",
    "answer = chatgpt.predict(\"코딩에 대한 시를 써줘\")\n",
    "print(answer.content)\n",
    "\n",
    "import streamlit as st\n",
    "\n",
    "st.set_page_config(\n",
    "    page_title=\"DirChat\",\n",
    "    page_icon=\":books:\")\n",
    "st.title(\"_Private Data :red[AA Chat]_ : books:\")\n",
    "\n",
    "with st.sidebar:\n",
    "    openai_api_key = st.text_input(\"OpenAI API key\", key=\"chatbot_api_key\", type=\"password\")\n",
    "    process = st.button(\"Process\")\n",
    "if process:\n",
    "    st.info(\"Please and your OpenAI API key to continue.\")\n",
    "    st.stop()\n",
    "\n",
    "content = st.text_input('시의 주제를 제시해주세요.')\n",
    "\n",
    "if st.button('시 작성 요청하기'):\n",
    "    with st.spinnet('시 작성 중...'):\n",
    "        result=chatgpt.predict(content + \"에 대한 시를 써줘\")\n",
    "        st.write(result)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
