import os
import json
from ai21 import AI21Client
from ai21.models.chat import ChatMessage, ResponseFormat

# Ensure the API key is set
api_key = os.getenv("AI21_API_KEY")
if not api_key:
    raise ValueError("API Key not found. Please export it in your terminal.")

# Initialize the AI21 Client
client = AI21Client(api_key=api_key)

def generate_blog_post(blog_topic):
    print(f"🔎 Researching topic: {blog_topic}")
    
    try:
        # Make the API call to AI21
        response = client.chat.completions.create(
            model="jamba-large-1.6",
            messages=[
                ChatMessage(role="system", content=f"Write a detailed blog post about {blog_topic}"),
                ChatMessage(role="user", content=f"Write a detailed blog post about {blog_topic}")
            ],
            n=1,
            max_tokens=1500,
            temperature=0.7,
            top_p=1,
            stop=[],
            response_format=ResponseFormat(type="text")
        )
        
        # Extract the response content
        blog_post_content = response.choices[0].message.content
        
        print("✅ Blog Post Generated Successfully!")

        # Save the blog post to a markdown file
        save_blog_post_to_file(blog_topic, blog_post_content)
        
    except Exception as e:
        print(f"❌ Error: Could not generate blog post\n{e}")

def save_blog_post_to_file(blog_topic, content):
    # Create a markdown file name from the topic
    filename = f"blog_post_{blog_topic.replace(' ', '_').lower()}.md"
    
    try:
        # Open the file in write mode and save the content
        with open(filename, 'w') as file:
            file.write(f"# {blog_topic}\n\n")
            file.write(content)
        
        print(f"📝 Blog post saved as {filename}")
    except Exception as e:
        print(f"❌ Error: Could not save blog post to file\n{e}")

if __name__ == "__main__":
    # Get the blog topic from the user
    blog_topic = input("Enter a blog topic: ")
    generate_blog_post(blog_topic)
