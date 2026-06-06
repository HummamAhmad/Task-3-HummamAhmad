"""
DecodeLabs Industrial Training Kit - Batch 2026
Project 3: Deep Cognitive Introspection and Multi-Layered Learning Ecosystem
Author: Hummam Ahmad
"""
import time
import difflib
import urllib.parse
import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
SHARED_VOCABULARY = ["Python", "Machine Learning", "Web Development", "Cloud Computing", "Data Science"]

INVERSE_DOMAIN_WEIGHTS = {
    "Python": 1.2,
    "Machine Learning": 2.5,
    "Web Development": 1.5,
    "Cloud Computing": 2.2,
    "Data Science": 2.0
}

CONCEPT_GLOSSARY_DATABASE = {
    "def": {
        "concept": "def (Python Keyword)",
        "description": "The command used to build a reusable block of code in Python. Think of it like defining a recipe once so you can cook it anytime by just calling its name.",
        "link": "https://www.youtube.com/watch?v=NE97cElcomk"
    },
    "class": {
        "concept": "class (Python Object-Oriented Programming)",
        "description": "A structural blueprint used to create customized objects. For example, a 'Car' class defines the basic layout (wheels, engine) so you can build specific cars from it.",
        "link": "https://www.youtube.com/watch?v=apACNr7Hg_0"
    },
    "lambda": {
        "concept": "lambda (Python Anonymous Functions)",
        "description": "A quick, single-line shorthand function that does not need a formal name. Used for short, throwaway math calculations or quick data transformations.",
        "link": "https://www.youtube.com/watch?v=hYzwCsK78Gs"
    },
    "with": {
        "concept": "with (Python Context Manager)",
        "description": "A safety tool that handles setup and cleanup files. When opening a file, it guarantees the file closes properly afterward, even if the program crashes.",
        "link": "https://www.youtube.com/watch?v=Lr0XkaP0wG4"
    },
    "yield": {
        "concept": "yield (Python Generators)",
        "description": "A smart alternative to 'return'. Instead of giving you a massive list all at once and eating up memory, it drips data out one single piece at a time.",
        "link": "https://www.youtube.com/watch?v=tmeKsb2Fras"
    },
    "decorators": {
        "concept": "Decorators (@ Syntax)",
        "description": "A clean way to modify or wrap the behavior of a function or class without permanently rewriting its internal logic.",
        "link": "https://www.youtube.com/watch?v=FsAPt_9Bf3U"
    },
    "list comprehensions": {
        "concept": "List Comprehensions",
        "description": "A compact, elegant syntax shorthand to create new Python lists out of existing sequences using concise single-line loops.",
        "link": "https://www.youtube.com/watch?v=3dt4OGnU5sM"
    },
    
    "os": {
        "concept": "os module (Operating System Abstraction)",
        "description": "A built-in library that lets Python speak directly to your computer's filesystem to create folders, delete files, or read system directories.",
        "link": "https://www.youtube.com/watch?v=tJxcKyFMTGo"
    },
    "sys": {
        "concept": "sys module (System Parameters and Functions)",
        "description": "Provides control over the internal Python engine. It tracks background system commands, argument inputs, and can force a script to stop running entirely.",
        "link": "https://www.youtube.com/watch?v=rcYnre06SRE"
    },
    "json": {
        "concept": "json module (JavaScript Object Notation Parser)",
        "description": "The translation tool used to convert nested text data into Python dictionaries and vice versa, which is critical for communicating with web systems.",
        "link": "https://www.youtube.com/watch?v=9N6a-VLBa2I"
    },
    
    "core concepts": {
        "concept": "Machine Learning: Core Concepts",
        "description": "Moving away from hardcoded commands toward models that look at data features (inputs) and learn to predict correct labels (outputs) on their own.",
        "link": "https://www.youtube.com/watch?v=GwIo3gBGUt0"
    },
    "data preparation": {
        "concept": "Machine Learning: Data Preparation",
        "description": "Cleaning messy data by filling missing cells (Imputation), adjusting varying scales (Scaling), and changing text into numbers so equations can read them.",
        "link": "https://www.youtube.com/watch?v=0xVqLJe9_CY"
    },
    "learning taxonomy": {
        "concept": "Machine Learning: Taxonomy Divisions",
        "description": "Dividing software models into Supervised Learning (where data has answers) and Unsupervised Learning (where models group unlabelled data by patterns).",
        "link": "https://www.youtube.com/watch?v=tKZTeKsc2xs"
    },
    "evaluation metrics": {
        "concept": "Machine Learning: Evaluation Metrics",
        "description": "Mathematical scoreboards (like Accuracy or RMSE error tracking) used to verify exactly how correct or skewed a model's real-world predictions are.",
        "link": "https://www.youtube.com/watch?v=2osIZ-dSPGE"
    },
    "fit": {
        "concept": "fit() method",
        "description": "The foundational training command in Machine Learning. It instructs an algorithm to analyze an array of data and adjust its mathematical weights to learn the patterns.",
        "link": "https://www.youtube.com/watch?v=b4O4VvIorKg"
    },
    "predict": {
        "concept": "predict() method",
        "description": "The execution command that takes an unlabelled input feature and runs it through a trained model to generate an optimized inference classification.",
        "link": "https://www.youtube.com/watch?v=b4O4VvIorKg"
    },
    "regression": {
        "concept": "Linear Regression / Continuous Prediction",
        "description": "A statistical supervised learning technique that models the mathematical relationship between input data features and a continuous, numerical output value.",
        "link": "https://www.youtube.com/watch?v=E5RjzSK0fvY"
    },
    
    "fetch": {
        "concept": "fetch() API (Web Development)",
        "description": "A browser mechanism used to request data or transfer information to a backend server asynchronously behind the scenes without refreshing the page.",
        "link": "https://www.youtube.com/watch?v=cuEtnrL9-H0"
    },
    "async/await": {
        "concept": "Asynchronous Programming (async/await)",
        "description": "Syntax that prevents a website from freezing up. It allows long network requests to finish while keeping the rest of your application completely interactive.",
        "link": "https://www.youtube.com/watch?v=V_Kr9OSfDeU"
    },
    "django": {
        "concept": "Django Web Framework & django.db ORM",
        "description": "A powerful high-level Python web framework designed for secure and fast development. It includes an Object-Relational Mapper (ORM) to interact with databases natively using Python classes.",
        "link": "https://www.youtube.com/watch?v=F5mRW0M-AGE"
    },
    "flask": {
        "concept": "Flask Web Framework",
        "description": "A lightweight micro web framework written in Python. It provides the absolute essentials to spin up backend servers and map endpoints quickly without structural overhead.",
        "link": "https://www.youtube.com/watch?v=Z1RJmh_OqeA"
    },
    
    "iam policy": {
        "concept": "IAM Policy (Identity & Access Management)",
        "description": "A secure rule blueprint that dictates exactly who is authorized to view or modify specific cloud infrastructure servers and database elements.",
        "link": "https://www.youtube.com/watch?v=YQsK4MtsYIs"
    },
    "vpc subnet": {
        "concept": "VPC Subnet (Virtual Private Cloud Network Slicing)",
        "description": "An isolated digital sandbox inside a cloud network used to isolate database assets and internal servers away from open public internet access.",
        "link": "https://www.youtube.com/watch?v=jZNv_ldw2w0"
    },
    "aws_s3_bucket": {
        "concept": "aws_s3_bucket (Terraform AWS Resource)",
        "description": "A dedicated Infrastructure as Code resource block used to declare, provision, configure, and maintain secure storage buckets on Amazon Web Services automatically.",
        "link": "https://www.youtube.com/watch?v=epD8L_p6V_c"
    },
    "terraform": {
        "concept": "Terraform (Infrastructure as Code)",
        "description": "An open-source automation tool that lets engineers define, version, and deploy cloud infrastructure across multiple providers securely using simple text configuration files.",
        "link": "https://www.youtube.com/watch?v=h970ZBgKINg"
    },

    "pandas": {
        "concept": "Pandas Data Analysis Library",
        "description": "The elite, go-to Python library built specifically for data handling and data manipulation. It introduces high-performance spreadsheet-like data structures.",
        "link": "https://www.youtube.com/watch?v=F6elz7U_8Bw"
    },
    "dataframe": {
        "concept": "Pandas DataFrame",
        "description": "An advanced, spreadsheet-like two-dimensional grid built inside Python memory. It gives you columns, rows, and heavy computational features to slice numbers.",
        "link": "https://www.youtube.com/watch?v=F6elz7U_8Bw"
    },
    "sklearn": {
        "concept": "Scikit-Learn (sklearn) Library",
        "description": "The standard machine learning library for Python. It contains pre-built utilities to split data arrays, build classification workflows, and execute performance metrics.",
        "link": "https://www.youtube.com/watch?v=0xVqLJe9_CY"
    }
}

DOMAIN_TAXONOMY_REGISTRY = {
    "python": {
        "title": "Core Python and Systems Architecture",
        "pillars": [{"text": "Pillar 1: Foundational Syntax, Control Flows, and Variable Scoping", "link": "https://www.youtube.com/watch?v=rfscVS0vtbw"},
                    {"text": "Pillar 2: Object-Oriented Programming (Classes & Inheritance)", "link": "https://www.youtube.com/watch?v=JeznW_7DlB0"},
                    {"text": "Pillar 3: Data Structures (Lists, Dicts, Tuples, Sets)", "link": "https://www.youtube.com/watch?v=RBAYaNMfN5k"},
                    {"text": "Pillar 4: Advanced Memory Mechanics (Generators, Context Managers)", "link": "https://www.youtube.com/watch?v=D1twnaa_A2U"}],
        "keywords": [{"text": CONCEPT_GLOSSARY_DATABASE["def"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["def"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["def"]["link"]},
                     {"text": CONCEPT_GLOSSARY_DATABASE["class"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["class"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["class"]["link"]},
                     {"text": CONCEPT_GLOSSARY_DATABASE["lambda"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["lambda"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["lambda"]["link"]},
                     {"text": CONCEPT_GLOSSARY_DATABASE["with"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["with"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["with"]["link"]},
                     {"text": CONCEPT_GLOSSARY_DATABASE["yield"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["yield"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["yield"]["link"]}],
        "submodules": [{"text": CONCEPT_GLOSSARY_DATABASE["os"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["os"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["os"]["link"]},
                       {"text": CONCEPT_GLOSSARY_DATABASE["sys"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["sys"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["sys"]["link"]},
                       {"text": CONCEPT_GLOSSARY_DATABASE["json"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["json"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["json"]["link"]}],
        "subroutines": [{"text": "print(): Outputs string representations of data directly to the terminal display.", "link": "https://www.youtube.com/watch?v=rfscVS0vtbw"}]
    },
    "machine learning": {
        "title": "Machine Learning Algorithmic Design and Optimization",
        "pillars": [{"text": "Pillar 1: Mathematical Foundations & Feature Engineering Patterns", "link": "https://www.youtube.com/watch?v=GwIo3gBGUt0"},
                    {"text": "Pillar 2: Supervised Learning Paradigms (Regression and Complex Classifiers)", "link": "https://www.youtube.com/watch?v=tKZTeKsc2xs"},
                    {"text": "Pillar 3: Unsupervised Deep Clustering Architecture Mechanisms", "link": "https://www.youtube.com/watch?v=tKZTeKsc2xs"},
                    {"text": "Pillar 4: Predictive Evaluation Models (Loss functions and Optimization Matrices)", "link": "https://www.youtube.com/watch?v=2osIZ-dSPGE"}],
        "keywords": [{"text": CONCEPT_GLOSSARY_DATABASE["fit"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["fit"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["fit"]["link"]},
                     {"text": CONCEPT_GLOSSARY_DATABASE["predict"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["predict"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["predict"]["link"]}],
        "submodules": [{"text": CONCEPT_GLOSSARY_DATABASE["sklearn"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["sklearn"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["sklearn"]["link"]}],
        "subroutines": [{"text": "train_test_split(): Slices rows into separate pattern extraction and checking assets.", "link": "https://www.youtube.com/watch?v=fw8g_g40Dk8"}]
    },
    "data science": {
        "title": "Data Science Analytics Pipeline and Empirical Wrangling",
        "pillars": [{"text": "Pillar 1: Exploratory Data Analysis (EDA Profiling and Null Imputation)", "link": "https://www.youtube.com/watch?v=F6elz7U_8Bw"},
                    {"text": "Pillar 2: Inferential Statistical Modeling and Hypothesis Metrics", "link": "https://www.youtube.com/watch?v=17Xp-Zz9Usw"},
                    {"text": "Pillar 3: Automated Data Engineering Pipelines & Cleansing Rules", "link": "https://www.youtube.com/watch?v=R9K1u9Zorv8"},
                    {"text": "Pillar 4: Visual Business Intelligence Layout Formats (Matplotlib / Seaborn)", "link": "https://www.youtube.com/watch?v=a9UrKTVEeZA"}],
        "keywords": [{"text": "DataFrame: High-performance tabular memory canvas configuration used for rows and columns operations.", "link": "https://www.youtube.com/watch?v=F6elz7U_8Bw"},
                     {"text": "Series: Single-dimensional structural data vector array modeling unique entity rows.", "link": "https://www.youtube.com/watch?v=F6elz7U_8Bw"}],
        "submodules": [{"text": CONCEPT_GLOSSARY_DATABASE["pandas"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["pandas"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["pandas"]["link"]}],
        "subroutines": [{"text": "read_csv(): Ingests external spreadsheet filesystem documents directly into RAM memory frames.", "link": "https://www.youtube.com/watch?v=F6elz7U_8Bw"}]
    },
    "web development": {
        "title": "Full-Stack Web Ecosystems and Async Network Protocols",
        "pillars": [{"text": "Pillar 1: HyperText Transfer Protocol Lifecycle (GET / POST Stateless Request Blocks)", "link": "https://www.youtube.com/watch?v=cuEtnrL9-H0"},
                    {"text": "Pillar 2: Client-Side Interactive DOM Control Interfaces", "link": "https://www.youtube.com/watch?v=V_Kr9OSfDeU"},
                    {"text": "Pillar 3: Multi-Layer Database Transaction Relational Mapping Mechanics", "link": "https://www.youtube.com/watch?v=F5mRW0M-AGE"},
                    {"text": "Pillar 4: Production Level Secure RESTful API Route Formats", "link": "https://www.youtube.com/watch?v=Z1RJmh_OqeA"}],
        "keywords": [{"text": CONCEPT_GLOSSARY_DATABASE["fetch"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["fetch"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["fetch"]["link"]},
                     {"text": CONCEPT_GLOSSARY_DATABASE["async/await"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["async/await"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["async/await"]["link"]}],
        "submodules": [{"text": CONCEPT_GLOSSARY_DATABASE["django"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["django"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["django"]["link"]},
                       {"text": CONCEPT_GLOSSARY_DATABASE["flask"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["flask"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["flask"]["link"]}],
        "subroutines": [{"text": "jsonify(): Formats backend dictionary structures into serialized web-safe data wrappers.", "link": "https://www.youtube.com/watch?v=Z1RJmh_OqeA"}]
    },
    "cloud computing": {
        "title": "Cloud Computing Infrastructure and Declarative IaC Architecture",
        "pillars": [{"text": "Pillar 1: Elastic Compute Virtual Machine Isolation Sandbox Rules", "link": "https://www.youtube.com/watch?v=jZNv_ldw2w0"},
                    {"text": "Pillar 2: Declarative Infrastructure State Definitions (IaC Engine Mechanics)", "link": "https://www.youtube.com/watch?v=h970ZBgKINg"},
                    {"text": "Pillar 3: High Availability Network Subnet Topology Maps", "link": "https://www.youtube.com/watch?v=jZNv_ldw2w0"},
                    {"text": "Pillar 4: Automated Cloud Identity Authentication Rules and Roles", "link": "https://www.youtube.com/watch?v=YQsK4MtsYIs"}],
        "keywords": [{"text": CONCEPT_GLOSSARY_DATABASE["aws_s3_bucket"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["aws_s3_bucket"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["aws_s3_bucket"]["link"]},
                     {"text": CONCEPT_GLOSSARY_DATABASE["iam policy"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["iam policy"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["iam policy"]["link"]},
                     {"text": CONCEPT_GLOSSARY_DATABASE["vpc subnet"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["vpc subnet"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["vpc subnet"]["link"]}],
        "submodules": [{"text": CONCEPT_GLOSSARY_DATABASE["terraform"]["concept"] + ": " + CONCEPT_GLOSSARY_DATABASE["terraform"]["description"], "link": CONCEPT_GLOSSARY_DATABASE["terraform"]["link"]}],
        "subroutines": [{"text": "terraform apply: Executes procedural instructions to construct infrastructure configurations on the cloud live.", "link": "https://www.youtube.com/watch?v=h970ZBgKINg"}]
    }
}

ITEM_DATABASE = [
    {"id": 101, "title": "Introduction to Python Programming", "tags": ["Python"]},
    {"id": 102, "title": "Advanced Machine Learning & Data Science Course", "tags": ["Python", "Machine Learning", "Data Science"]},
    {"id": 103, "title": "Full-Stack Web Development Bootcamp", "tags": ["Web Development"]},
    {"id": 104, "title": "Cloud Computing Infrastructure with AWS", "tags": ["Cloud Computing"]},
    {"id": 105, "title": "Data Science Fundamentals and Data Analytics", "tags": ["Python", "Data Science"]},
    {"id": 106, "title": "Modern Web Apps with Python Flask & Django", "tags": ["Python", "Web Development"]}
]

def text_to_binary_vector(tags_list, vocabulary):
    return [1 if tag in tags_list else 0 for tag in vocabulary]

def calculate_weighted_jaccard(vector_user, vector_item, vocabulary, weights):
    intersection_weight = 0.0
    union_weight = 0.0
    for idx, tag in enumerate(vocabulary):
        weight = weights.get(tag, 1.0)
        user_has_it = vector_user[idx]
        item_has_it = vector_item[idx]
        if user_has_it and item_has_it:
            intersection_weight += weight
            union_weight += weight
        elif user_has_it or item_has_it:
            union_weight += weight
    return intersection_weight / union_weight if union_weight > 0 else 0.0

def get_closest_local_match(query, database_keys):
    query = query.lower().strip()
    for key in database_keys:
        if query == key or (len(query) >= 3 and query in key):
            return key
    matches = difflib.get_close_matches(query, list(database_keys), n=1, cutoff=0.65)
    if matches:
        return matches[0]
    return None

def execute_live_web_crawl(query):
    """
    Dual-Route Live Web Search:
    1. Grabs a structured textbook-style text explanation from the internet index.
    2. Dynamically scours the search index to pull an exact YouTube tutorial link for the query.
    """
    print(f"   [📡 LOCAL CACHE MISS] Querying live web index safely for '{query}'...")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    text_query = urllib.parse.quote_plus(f"what is {query} concept definition explanation")
    text_url = f"https://html.duckduckgo.com/html/?q={text_query}"
    
    yt_query = urllib.parse.quote_plus(f"{query} programming tutorial video youtube")
    yt_url = f"https://html.duckduckgo.com/html/?q={yt_query}"
    
    clean_desc = ""
    video_link = f"https://www.youtube.com/results?search_query={urllib.parse.quote_plus(query)}"

    try:
        response = requests.get(text_url, headers=headers, timeout=5, verify=False)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            snippets = soup.find_all('a', class_='result__snippet')
            if snippets:
                clean_desc = snippets[0].get_text().strip()
                sentences = [s.strip() for s in clean_desc.replace('!', '.').replace('?', '.').split('.') if s.strip()]
                refined = [s for s in sentences if not any(w in s.lower() for w in ["github", "code example", "click here", "read more"])]
                clean_desc = ". ".join(refined[:2]) + "." if refined else clean_desc
    except Exception:
        pass

    if not clean_desc or len(clean_desc) < 15:
        clean_desc = f"An advanced engineering module, cloud script component, or algorithmic framework element utilized in production-scale codebases to manage and process {query.upper()} operations."

    if not any(clean_desc.lower().startswith(x) for x in ["a ", "an ", "the ", query.lower()]):
        clean_desc = f"{query} is a " + clean_desc[0].lower() + clean_desc[1:]

    try:
        yt_response = requests.get(yt_url, headers=headers, timeout=5, verify=False)
        if yt_response.status_code == 200:
            yt_soup = BeautifulSoup(yt_response.text, 'html.parser')
            links = yt_soup.find_all('a', class_='result__url')
            
            for link in links:
                href = link.get('href', '')
                if "youtube.com" in href or "youtu.be" in href:
                    if "uddg=" in href:
                        try:
                            parsed_url = urllib.parse.urlparse(href)
                            query_params = urllib.parse.parse_qs(parsed_url.query)
                            if 'uddg' in query_params:
                                video_link = query_params['uddg'][0]
                                break
                        except Exception:
                            video_link = urllib.parse.unquote(href.split("uddg=")[1].split("&")[0])
                            break
                    else:
                        if href.startswith("//"):
                            href = "https:" + href
                        video_link = href
                        break
    except Exception:
        pass

    return {
        "concept": query,
        "description": clean_desc,
        "link": video_link
    }
    
def run_concept_search_vault():
    print("\n--- HYBRID CONCEPT SEARCH VAULT [LIVE CONNECTIVITY ACTIVE] ---")
    print("What specific tech concept or command are you thinking of or looking for today?")
    user_query = input("Search Concept >> ").strip()
    
    if not user_query:
        return

    matched_key = get_closest_local_match(user_query, CONCEPT_GLOSSARY_DATABASE.keys())
    
    if matched_key:
        data = CONCEPT_GLOSSARY_DATABASE[matched_key]
        print("\n------------------------------------------------------------")
        print(f"Target Concept Found: {data['concept']} [LOCAL REGISTRY MATCH]")
        print(f"Simplified Explanation: {data['description']}")
        print(f"Explaining Video Link: {data['link']}")
        print("------------------------------------------------------------")
    else:
        live_data = execute_live_web_crawl(user_query)
        
        if live_data:
            print("\n------------------------------------------------------------")
            print(f"Target Concept Found: {live_data['concept']} [DYNAMIC WEB EXTRACTION]")
            print(f"Simplified Explanation: {live_data['description']}")
            print(f"Explaining Video Link: {live_data['link']}")
            print("------------------------------------------------------------")
        else:
            print("\n[!] Not Found: The term is missing locally and couldn't be resolved via backup crawler.")
    
    input("\n[Press Enter to return to main tracking deck...]")

def parse_flexible_input(user_raw_string):
    raw_tokens = [token.strip().lower() for token in user_raw_string.split(",") if token.strip()]
    matched_tags = set()
    shortcut_map = {"py": "Python", "ml": "Machine Learning", "web": "Web Development", "aws": "Cloud Computing", "ds": "Data Science"}
    
    for token in raw_tokens:
        if token in shortcut_map:
            matched_tags.add(shortcut_map[token])
            continue
        for official_tag in SHARED_VOCABULARY:
            if token == official_tag.lower() or token in official_tag.lower():
                matched_tags.add(official_tag)
    return list(matched_tags)

def print_structured_layer(items, label_string):
    print(f"\n[{label_string}]:")
    for item in items:
        print(f"   - {item['text']}")
        print(f"     Target Video Concept Search: {item['link']}")

def execute_deep_dive_loop(selected_tags):
    print("\n--- KNOWLEDGE LAYER DISCOVERY MODULE ---")
    print("Would you like to explore structural pillars or syntax submodules for these domains? (yes/no)")
    choice = input(">> ").strip().lower()
    
    if choice not in ['yes', 'y', 'sure']:
        return
        
    while True:
        print("\nSelected domains ready for structural inspection:")
        for idx, tag in enumerate(selected_tags, 1):
            print(f"   [{idx}] {tag}")
        print("\nSelect a domain index number to unpack (or type 'back' to return to main loop):")
        domain_choice = input(">> ").strip()
        
        if domain_choice.lower() == 'back':
            break
            
        if not domain_choice.isdigit() or int(domain_choice) < 1 or int(domain_choice) > len(selected_tags):
            print("[!] Validation Error: Invalid selection index.")
            continue
            
        target_domain = selected_tags[int(domain_choice) - 1].lower()
        taxonomy = DOMAIN_TAXONOMY_REGISTRY.get(target_domain)
        
        if not taxonomy:
            print("[!] System Exception: Structural map missing or unconfigured for this domain.")
            continue
            
        while True:
            print(f"\n[TARGET DIRECTORY]: {taxonomy['title']}")
            print("What specific architectural layer do you want to analyze?")
            print("  1. Foundational System Pillars")
            print("  2. System Keywords / Logic Tokens")
            print("  3. Library Submodules / Framework Bundles")
            print("  4. Core Subroutines / Executable Methods")
            print("  5. [Switch Active Domain Area]")
            layer_choice = input("Select option [1-5] >> ").strip()
            
            if layer_choice == '5':
                break
            elif layer_choice == '1':
                print_structured_layer(taxonomy['pillars'], f"FOUNDATIONAL ARCHITECTURAL PILLARS FOR {target_domain.upper()}")
            elif layer_choice == '2':
                print_structured_layer(taxonomy['keywords'], f"VITAL LOGIC KEYS AND SYMBOL TOKENS FOR {target_domain.upper()}")
            elif layer_choice == '3':
                print_structured_layer(taxonomy['submodules'], f"STANDARD SUBMODULE EXTENSIONS FOR {target_domain.upper()}")
            elif layer_choice == '4':
                print_structured_layer(taxonomy['subroutines'], f"EXECUTABLE SUBROUTINES AND CORE FUNCTIONS FOR {target_domain.upper()}")
            else:
                print("[!] Selection Out of Bounds. Choose an option between 1 and 5.")
                
            print("\n------------------------------------------------------------")
            input("[Press Enter to view the option menu again...]")

def main():
    print("========================================================================")
    print("      DECODELABS COGNITIVE PREDICTIVE ENVIRONMENT [INTELLISENSE ACTIVE]      ")
    print("========================================================================")
    
    while True:
        print("\nWhat core operation mode do you want to access?")
        print("  1. General Career Track Recommendation Mapper")
        print("  2. Instant Tech Concept / Command Search Vault")
        print("  3. Exit Program")
        mode_choice = input("Select Mode [1-3] >> ").strip()

        if mode_choice == '3':
            print("\n[+] Exporting project state logs to origin master branches. Goodbye!")
            break
            
        elif mode_choice == '2':
            run_concept_search_vault()
            continue
            
        elif mode_choice == '1':
            print("\nIndustry Vectors Managed inside Active Engine Memory:")
            print("  » Python (py)           » Machine Learning (ml)   » Web Development (web)")
            print("  » Cloud Computing (aws)  » Data Science (ds)")
            print("------------------------------------------------------------------------")
            print("Enter your career interest domains (separate fields with commas):")
            user_input = input(">> ")
            
            selected_tags = parse_flexible_input(user_input)
            if not selected_tags:
                print("\n[!] Input Evaluation Error: No matches found in vocabulary arrays.")
                continue

            if any(t in selected_tags for t in ["Machine Learning", "Data Science"]) and "Python" not in selected_tags:
                print("\n[AI INFERENCE INTERCEPT]: Advanced data structures require procedural functional mapping.")
                print("   The engine has automatically appended 'Python' as a compulsory prerequisite vector.")
                selected_tags.append("Python")
                time.sleep(1)

            user_vector = text_to_binary_vector(selected_tags, SHARED_VOCABULARY)
            scored_catalog = []
            for item in ITEM_DATABASE:
                item_vector = text_to_binary_vector(item["tags"], SHARED_VOCABULARY)
                similarity = calculate_weighted_jaccard(user_vector, item_vector, SHARED_VOCABULARY, INVERSE_DOMAIN_WEIGHTS)
                
                scored_item = item.copy()
                scored_item["score"] = round(similarity, 4)
                scored_catalog.append(scored_item)
                
            scored_catalog.sort(key=lambda x: x["score"], reverse=True)
            
            print("\n========================================================================")
            print("                      YOUR CUSTOMIZED AI LEARNING TRACK MAP                    ")
            print("========================================================================")
            for rank, match in enumerate(scored_catalog[:3], 1):
                print(f"Rank {rank} | Structural Alignment Profile: {round(match['score'] * 100, 2)}%")
                print(f"       Course: {match['title']}")
                print(f"       Attributes: {match['tags']}")
                print("------------------------------------------------------------------------")
                
            execute_deep_dive_loop(selected_tags)

if __name__ == "__main__":
    main()