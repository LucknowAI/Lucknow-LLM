<div align="center">
<h1>lucknow LLM</h1></div>

<p align="center">
  <p align="center">Lucknow LLM
</p>
</p>

 <h4 align="center">
  <a href="https://github.com/LucknowAI/Lucknow-LLM/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="Promptify is released under the Apache 2.0 license." />
  </a>
  <a href="https://pypi.org/project/Lucknow-LLM/">
    <img src="https://badge.fury.io/py/Lucknow-LLM.svg" alt="PyPI version" />
  </a>
  <a href="http://makeapullrequest.com">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="http://makeapullrequest.com" />
  </a>
  <a href="https://discord.gg/QKw67PDZUm">
    <img src="https://img.shields.io/badge/Discord-Community-orange" alt="Community" />
  </a>
  <a href="https://github.com/LucknowAI/Lucknow-LLM/blob/main/notebooks/data_pipeline.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="colab" />
  </a>
</h4>

## Installation

### With pip

You should install lucknowllm using Pip command

```bash
pip3 install git+https://github.com/LucknowAI/Lucknow-LLM.git
```

## Quick tour of LucknowLLM Framework

How to get prompt

```python
from lucknowllm import construct_prompt
construct_prompt('raw_to_structured', "Hello world, This is input sentence")
```

How to convert raw data into structured data

```python
from lucknowllm import get_prompt
from lucknowllm import GeminiModel

Gemini = GeminiModel(api_key = "", model_name = "gemini-1.0-pro")

llm_input    = construct_prompt('raw_to_structured', "Lucknow is the capital and the largest city of the Indian state of Uttar Pradesh and it is the administrative headquarters of the eponymous district and division.")
model_output = Gemini.generate_content(llm_input)
```

How to segment long Paragraphs into smaller ones for the model input

```python
from lucknowllm import split_into_segments

sentence = "Lucknow is the capital and the largest city of the Indian state of Uttar Pradesh and it is the administrative headquarters of the eponymous district and division."
split_into_segments(sentence)
```

How to load Unstructured Data

```python
from lucknowllm import UnstructuredDataLoader
loader = UnstructuredDataLoader()

# if you want to load all files in one folder
loader.get_data('Cultural_Festival_of_Lucknow')

#if you want to load specific file
loader.get_data('Cultural_Festival_of_Lucknow', 'Lucknow_Mahotsav.txt')
```

How to load structured Data

```python
from lucknowllm import StructuredDataLoader
loader = StructuredDataLoader()

# if you want to load all files in one folder
loader.get_data('Arts_and_Crafts')

#if you want to load specific file
loader.get_data('Arts_and_Crafts', 'Arts_and_Craft.json')
```

<h2>Contributing to LucknowLLM</h2>

<p>You can contribute in the following ways:</p>

<h3>Collect Unstructured Data</h3>
<p>Choose a topic from the list below and search for content related to Lucknow on the internet, books, newspapers, or wherever you can find relevant information. If the topic is not listed, you can create a new topic and contribute.</p>

<h3>Contribute to the LucknowLLM Framework</h3>
<p>You can help build the LucknowLLM framework by working on the data preprocessing pipeline, collecting data automatically using Selenium, website scrapers, etc. Write scripts for these tasks and contribute them, and provide tutorials for those scripts in the <code>tutorial</code> folder to make them easy to understand and use.</p>

<h3>Review Dataset Quality</h3>
<p>You can contribute as a reviewer to ensure the quality of the dataset. Go through existing datasets in <a href="https://github.com/LucknowAI/Lucknow-LLM/tree/main/lucknowllm/data/Unstructured_data">lucknowllm/data/Unstructured_data</a> and check their quality. If you find any biased, aggressive, religiously or politically biased, or sensitive information, you can remove it. This is also a valuable contribution to maintaining the quality of the datasets.</p>

<h3>Contribute to Documentation</h3>
<p>You can contribute to the documentation of the LucknowLLM framework. We can have a website like <a href="https://lucknowllm.readthedocs.io" target="_blank">lucknowllm.readthedocs.io</a> where users can understand how to use the framework. Check out <a href="https://about.readthedocs.com/?ref=readthedocs.com" target="_blank">https://about.readthedocs.com/?ref=readthedocs.com</a> for more information.</p>

<h3>Improve the Lucknow AI Website</h3>
<p>You can also work on improving the content of the Lucknow AI website. Check out <a href="https://github.com/LucknowAI/lucknowai.github.io" target="_blank">https://github.com/LucknowAI/lucknowai.github.io</a> for more details.</p>


### How to Start? I'm New to GitHub

- **Tutorial:** <a href="https://www.youtube.com/watch?v=2LOyAnFuw8Y" target="_blank">https://www.youtube.com/watch?v=2LOyAnFuw8Y</a>
- **Create a GitHub profile.**
- **Fork the repository.** Tutorial: <a href="https://www.youtube.com/watch?v=NZIsGcCtvzw" target="_blank">https://www.youtube.com/watch?v=NZIsGcCtvzw</a>
- **Choose where you can contribute.** See the contribution guide above.
- **Edit content in your forked repository and submit a pull request.** We'll review the request and merge it into the main branch.

## Collecting data for Building Lucknow's first LLM

We are planning to collect these categories of data (not limited to):</p>

<ul>

  <li><strong>Overview of Lucknow:</strong> A comprehensive introduction to Lucknow, covering its history, culture, and key characteristics.</li>
  <li><strong>Food of Lucknow:</strong> An exploration of Lucknow's culinary scene, detailing its diverse dishes, renowned restaurants, and must-visit food places.</li>
  <li><strong>Tourism in Lucknow:</strong> A guide to Lucknow's tourist attractions, including historical sites, cultural landmarks, and recreational spots.</li>
  
  <li><strong>History of Lucknow:</strong> Detailed information on historical events, significant figures, and the architectural heritage of Lucknow.</li>

  <li><strong>Cultural Festivals of Lucknow:</strong> Information on local festivals, celebrations, and cultural events that take place throughout the year.</li>

  <li><strong>Economy and Industries of Lucknow:</strong> Insights into the local economy, major industries, employment opportunities, and economic development.</li>

  <li><strong>Transportation in Lucknow:</strong> Data on public transport systems, major roads, railway connectivity, and airport information.</li>

  <li><strong>Education System in Lucknow:</strong> Details on primary, secondary, and higher education institutions beyond colleges, including special educational programs and vocational training centers.</li>

  <li><strong>Healthcare in Lucknow:</strong> Information on hospitals, clinics, healthcare services, and health initiatives.</li>

  <li><strong>Politics and Governance of Lucknow:</strong> Insights into the local government structure, political landscape, significant political events, and governance policies.</li>

  <li><strong>Sports and Recreation in Lucknow:</strong> Details on sports facilities, local sports teams, recreational areas, and sports events.</li>

  <li><strong>Media in Lucknow:</strong> Information on local newspapers, radio stations, television channels, and digital media platforms.</li>

  <li><strong>Art and Literature of Lucknow:</strong> Insights into the local art scene, literature, notable artists, writers from Lucknow, and cultural institutions promoting art and literature.</li>

  <li><strong>Environmental Initiatives in Lucknow:</strong> Information on green spaces, pollution control measures, sustainability projects, and environmental awareness programs.</li>

  <li><strong>Social Issues and Development in Lucknow:</strong> Insights into social challenges, community development projects, and NGOs working in Lucknow.</li>

  <li><strong>Technology and Innovation in Lucknow:</strong> Data on tech startups, innovation hubs, IT parks, and technology education programs.</li>

  <li><strong>Local Businesses and Entrepreneurs in Lucknow:</strong> Information on local markets, famous shops, entrepreneurs, and success stories of local businesses.</li>

  <li><strong>Famous Personalities from Lucknow:</strong> Biographies and contributions of notable figures in various fields such as arts, sciences, sports, and politics who hail from Lucknow.</li>

  <li><strong>Religious Places in Lucknow:</strong> Information on temples, mosques, churches, and other places of worship, including their historical significance and cultural importance.</li>

  <li><strong>Lucknow's Cuisine Varieties Beyond the Basics:</strong> Exploring lesser-known dishes, street food culture, and culinary traditions unique to Lucknow.</li>
</ul>


# Websites to scrape

<li><strong>Wikipedia Lucknow</li>
<li><strong>https://uptourism.gov.in/</li>


## Hall-Of-Fame | Top Contributors

<a href="https://github.com/LucknowAI/Lucknow-LLM-data/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=LucknowAI/Lucknow-LLM-data" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
