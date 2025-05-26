import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# Function to get response from LLaMA 2 model
def getLLamaresponse(input_text, no_words, blog_style):
    # Load model
    llm = CTransformers(
        model='Models/llama-2-7b-chat.ggmlv3.q8_0.bin',
        model_type='llama',
        config={
            'max_new_tokens': 256,
            'temperature': 0.01
        }
    )

    # Prompt template
    template = """
    Write a blog for a {blog_style} job profile on the topic "{input_text}" within {no_words} words.
    """
    prompt = PromptTemplate(
        input_variables=["blog_style", "input_text", "no_words"],
        template=template
    )

    # Format and invoke
    formatted_prompt = prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words)
    response = llm.invoke(formatted_prompt)
    return response

# Streamlit App UI
st.set_page_config(page_title="Generate Blogs", page_icon='🤖', layout='centered', initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")
input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5, 5])
with col1:
    no_words = st.text_input('No of words')
with col2:
    blog_style = st.selectbox('Writing the blog for', ('Researchers', 'Data Scientist', 'Common people'), index=0)

submit = st.button("Generate")

if submit:
    with st.spinner("Generating blog..."):
        response = getLLamaresponse(input_text, no_words, blog_style)
        st.subheader("Generated Blog ✨")
        st.write(response)
