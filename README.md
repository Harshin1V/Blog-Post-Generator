# AI-Based Blog Post Generator

This project is an AI-powered blog post generation tool that leverages the AI21 API to generate detailed and high-quality blog posts based on a given topic. The tool takes a user's input (blog topic), queries the AI21 language model, and generates a blog post, which is then saved as a markdown file.

## Features

- **AI-Powered Content Generation**: Uses AI21's advanced language model to generate detailed blog posts on any given topic.
- **User-Friendly Input**: Takes a blog topic as input from the user.
- **Markdown Output**: Saves the generated blog post in a `.md` (markdown) file.
- **Error Handling**: Includes error handling to manage API call failures and save issues.
- **Easy to Extend**: Easily extendable to generate other types of content (e.g., emails, social media posts).

## Technologies

- **Python**: The programming language used to build the tool.
- **AI21 API**: Used for natural language processing and content generation.
- **JSON**: For handling the responses from the AI21 API.
- **File I/O**: For saving the generated content to a markdown file.
  
## Setup and Installation

### Prerequisites

- Python 3.6 or higher
- An **AI21 API Key** (You can get your API key by signing up at [AI21 Studio](https://studio.ai21.com/)).
  
### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-blog-post-generator.git
cd ai-blog-post-generator
```

### 2. Install required dependencies

It is recommended to set up a virtual environment to manage dependencies.

```bash
python3 -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Set up your API Key

Before running the script, ensure that your API key is set as an environment variable.

For macOS/Linux:

```bash
export AI21_API_KEY="your_api_key_here"
```


Alternatively, you can directly replace `os.getenv("AI21_API_KEY")` with your API key in the script (not recommended for security reasons).

### 4. Run the project

```bash
python test.py
```

### 5. Enter a Blog Topic

When prompted, enter the topic for the blog post you want to generate.

```bash
Enter a blog topic: AI trends in 2025
```

The script will generate a blog post based on your input and save it as a markdown file.

## Output

After running the script, the generated blog post will be saved as a `.md` file, such as:

```
blog_post_ai_trends_in_2025.md
```

The markdown file will contain the full content of the generated blog post.

## Example

Input:

```
Enter a blog topic: AI trends in 2025
```

Output:

```
📝 Blog post saved as blog_post_ai_trends_in_2025.md
```

## Troubleshooting

- **Error: Could not generate blog post**  
  Ensure that your API key is correctly set and that you are connected to the internet.

- **Error: Could not save blog post to file**  
  Check if you have write permissions in the directory where the script is being executed.

## Future Enhancements

- **Web Interface**: Create a simple web interface using frameworks like Flask or Streamlit.
- **Model Customization**: Allow the user to customize the tone, length, or style of the blog post.
- **Support for Other Content Types**: Extend the tool to generate other types of content like social media posts or email drafts.

