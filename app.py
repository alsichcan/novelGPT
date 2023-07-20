import os
import numpy as np
import pandas as pd
import openai
from openai.embeddings_utils import distances_from_embeddings
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]

        df=pd.read_csv('embedded_novel.csv', encoding='utf-8')
        df['embedding'] = df['embedding'].apply(eval).apply(np.array)

        response = answer_question(df, question=question, debug=True)

        return redirect(url_for("index", result=response))

    result = request.args.get("result")
    return render_template("index.html", result=result)

def create_context(
    question, df, max_len=1800, size="ada"
):
    """
    Create a context for a question by finding the most similar context from the dataframe
    """
    # Get the embeddings for the question
    q_embeddings = openai.Embedding.create(input=question, engine='text-embedding-ada-002')['data'][0]['embedding']

    # Get the distances from the embeddings
    df['distances'] = distances_from_embeddings(q_embeddings, df['embedding'].values, distance_metric='cosine')

    returns = []
    # Sort by distance and add the text to the context until the context is too long
    for i, row in df.sort_values('distances', ascending=True).iterrows():
        returns.append(f"Episode: {row['Episode']}, Content: {row['Content']}")

    # Return the context
    return "\n\n###\n\n".join(returns[:4])


def answer_question(
    df,
    question,
    model="text-davinci-003",
    max_len=1800,
    size="ada",
    debug=False,
    max_tokens=1000,
    stop_sequence=None
):
    """
    Answer a question based on the most similar context from the dataframe texts
    """
    context = create_context(
        question,
        df,
        max_len=max_len,
        size=size,
    )
    # If debug, print the raw model response
    if debug:
        print("Context:\n" + context)
        print("\n\n")

    try:
        # Create a completions using the question and context
        response = openai.Completion.create(
            prompt=f"Answer the question based on the context below\n\nContext: {context}\n\n---\n\nQuestion: {question}\nAnswer:",
            temperature=0.5,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=stop_sequence,
            model=model,
        )
        return response["choices"][0]["text"].strip()
    except Exception as e:
        print(e)
        return ""
