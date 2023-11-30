from loguru import logger
from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()


class TransformerSummarizer:
    """
    Summarizer using gpt2
    """

    def get_summarized_text(self, text_to_be_summarized):
        llm = HuggingFaceHub(
            repo_id="facebook/bart-large-cnn", model_kwargs={"temperature": 0.8}
        )
        question = text_to_be_summarized
        template = "Give a descriptive summary of the text which is starting after colon: {text_to_be_summarized}"

        prompt = PromptTemplate(template=template, input_variables=["text_to_be_summarized"])
        llm_chain = LLMChain(prompt=prompt, llm=llm)
        logger.info("Created LLM chain to summarise text")
        summary = llm_chain.run(question)
        logger.info("Summary is ready to be picked up")
        return summary.lstrip().rstrip()
