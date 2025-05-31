# import streamlit as st
# import json
# import random
# import re
# from typing import List, Dict, Any
# from dataclasses import dataclass
# from datetime import datetime

# # Recipe data structure
# @dataclass
# class Recipe:
#     name: str
#     ingredients: List[str]
#     instructions: List[str]
#     prep_time: int
#     cook_time: int
#     servings: int
#     difficulty: str
#     cuisine: str
#     category: str

# class RecipeGenerator:
#     def __init__(self):
#         self.recipes_db = self._initialize_recipe_database()
#         self.ingredient_substitutions = self._initialize_substitutions()
    
#     def _initialize_recipe_database(self) -> List[Recipe]:
#         """Initialize with sample recipes"""
#         return [
#             Recipe(
#                 name="Classic Spaghetti Carbonara",
#                 ingredients=[
#                     "400g spaghetti",
#                     "200g pancetta or bacon, diced",
#                     "4 large eggs",
#                     "100g Pecorino Romano cheese, grated",
#                     "2 cloves garlic, minced",
#                     "Black pepper to taste",
#                     "Salt for pasta water"
#                 ],
#                 instructions=[
#                     "Bring a large pot of salted water to boil and cook spaghetti according to package directions.",
#                     "While pasta cooks, fry pancetta in a large skillet until crispy.",
#                     "In a bowl, whisk together eggs, cheese, and black pepper.",
#                     "Reserve 1 cup pasta water before draining.",
#                     "Add hot pasta to the skillet with pancetta.",
#                     "Remove from heat and quickly stir in egg mixture, adding pasta water as needed.",
#                     "Serve immediately with extra cheese and pepper."
#                 ],
#                 prep_time=15,
#                 cook_time=20,
#                 servings=4,
#                 difficulty="Medium",
#                 cuisine="Italian",
#                 category="Pasta"
#             ),
#             Recipe(
#                 name="Chicken Stir Fry",
#                 ingredients=[
#                     "500g chicken breast, sliced thin",
#                     "2 bell peppers, sliced",
#                     "1 onion, sliced",
#                     "2 carrots, julienned",
#                     "3 cloves garlic, minced",
#                     "2 tbsp soy sauce",
#                     "1 tbsp oyster sauce",
#                     "1 tsp sesame oil",
#                     "2 tbsp vegetable oil",
#                     "1 tsp cornstarch",
#                     "Green onions for garnish"
#                 ],
#                 instructions=[
#                     "Marinate chicken with soy sauce and cornstarch for 15 minutes.",
#                     "Heat vegetable oil in a wok or large skillet over high heat.",
#                     "Stir-fry chicken until cooked through, remove and set aside.",
#                     "Add more oil if needed, stir-fry vegetables until crisp-tender.",
#                     "Return chicken to wok, add sauces and sesame oil.",
#                     "Stir everything together for 2 minutes.",
#                     "Garnish with green onions and serve with rice."
#                 ],
#                 prep_time=20,
#                 cook_time=15,
#                 servings=4,
#                 difficulty="Easy",
#                 cuisine="Asian",
#                 category="Main Course"
#             ),
#             Recipe(
#                 name="Chocolate Chip Cookies",
#                 ingredients=[
#                     "2 1/4 cups all-purpose flour",
#                     "1 tsp baking soda",
#                     "1 tsp salt",
#                     "1 cup butter, softened",
#                     "3/4 cup granulated sugar",
#                     "3/4 cup brown sugar",
#                     "2 large eggs",
#                     "2 tsp vanilla extract",
#                     "2 cups chocolate chips"
#                 ],
#                 instructions=[
#                     "Preheat oven to 375°F (190°C).",
#                     "Mix flour, baking soda, and salt in a bowl.",
#                     "Cream butter and sugars until fluffy.",
#                     "Beat in eggs and vanilla.",
#                     "Gradually mix in flour mixture.",
#                     "Stir in chocolate chips.",
#                     "Drop rounded tablespoons onto ungreased baking sheets.",
#                     "Bake 9-11 minutes until golden brown.",
#                     "Cool on baking sheet for 2 minutes before removing."
#                 ],
#                 prep_time=15,
#                 cook_time=10,
#                 servings=24,
#                 difficulty="Easy",
#                 cuisine="American",
#                 category="Dessert"
#             ),
#             Recipe(
#                 name="Caesar Salad",
#                 ingredients=[
#                     "1 large head romaine lettuce, chopped",
#                     "1/2 cup mayonnaise",
#                     "2 cloves garlic, minced",
#                     "2 tbsp lemon juice",
#                     "1 tsp Worcestershire sauce",
#                     "1 tsp Dijon mustard",
#                     "1/2 cup Parmesan cheese, grated",
#                     "1/2 cup croutons",
#                     "Salt and pepper to taste"
#                 ],
#                 instructions=[
#                     "Wash and chop romaine lettuce, pat dry.",
#                     "In a large bowl, whisk together mayonnaise, garlic, lemon juice, Worcestershire, and mustard.",
#                     "Add lettuce and toss to coat.",
#                     "Sprinkle with Parmesan cheese and croutons.",
#                     "Season with salt and pepper.",
#                     "Serve immediately."
#                 ],
#                 prep_time=15,
#                 cook_time=0,
#                 servings=4,
#                 difficulty="Easy",
#                 cuisine="American",
#                 category="Salad"
#             ),
#             Recipe(
#                 name="Beef Tacos",
#                 ingredients=[
#                     "1 lb ground beef",
#                     "1 onion, diced",
#                     "2 cloves garlic, minced",
#                     "1 packet taco seasoning",
#                     "1/4 cup water",
#                     "8 taco shells",
#                     "1 cup shredded lettuce",
#                     "1 cup shredded cheese",
#                     "2 tomatoes, diced",
#                     "1/2 cup sour cream",
#                     "Salsa for serving"
#                 ],
#                 instructions=[
#                     "Cook ground beef and onion in a large skillet until beef is browned.",
#                     "Add garlic and cook for 1 minute.",
#                     "Stir in taco seasoning and water, simmer for 5 minutes.",
#                     "Warm taco shells according to package directions.",
#                     "Fill shells with beef mixture.",
#                     "Top with lettuce, cheese, tomatoes, and sour cream.",
#                     "Serve with salsa."
#                 ],
#                 prep_time=10,
#                 cook_time=15,
#                 servings=4,
#                 difficulty="Easy",
#                 cuisine="Mexican",
#                 category="Main Course"
#             ),
#             Recipe(
#                 name="Mushroom Risotto",
#                 ingredients=[
#                     "1 1/2 cups Arborio rice",
#                     "4 cups warm chicken broth",
#                     "1 cup mixed mushrooms, sliced",
#                     "1/2 cup white wine",
#                     "1 onion, finely diced",
#                     "3 cloves garlic, minced",
#                     "1/2 cup Parmesan cheese, grated",
#                     "3 tbsp butter",
#                     "2 tbsp olive oil",
#                     "Salt and pepper to taste",
#                     "Fresh parsley for garnish"
#                 ],
#                 instructions=[
#                     "Heat olive oil and 1 tbsp butter in a large pan.",
#                     "Sauté mushrooms until golden, remove and set aside.",
#                     "In the same pan, cook onion until translucent.",
#                     "Add garlic and rice, stir for 2 minutes.",
#                     "Add wine and stir until absorbed.",
#                     "Add warm broth one ladle at a time, stirring constantly.",
#                     "Continue until rice is creamy and tender (about 18-20 minutes).",
#                     "Stir in mushrooms, remaining butter, and Parmesan.",
#                     "Season with salt and pepper, garnish with parsley."
#                 ],
#                 prep_time=15,
#                 cook_time=30,
#                 servings=4,
#                 difficulty="Hard",
#                 cuisine="Italian",
#                 category="Main Course"
#             )
#         ]
    
#     def _initialize_substitutions(self) -> Dict[str, List[str]]:
#         """Initialize ingredient substitutions"""
#         return {
#             "butter": ["margarine", "coconut oil", "vegetable oil"],
#             "milk": ["almond milk", "soy milk", "oat milk"],
#             "eggs": ["flax eggs", "chia eggs", "applesauce"],
#             "flour": ["almond flour", "coconut flour", "gluten-free flour"],
#             "sugar": ["honey", "maple syrup", "stevia"],
#             "chicken": ["tofu", "tempeh", "mushrooms"],
#             "beef": ["lentils", "black beans", "portobello mushrooms"]
#         }
    
#     def search_by_ingredients(self, available_ingredients: List[str]) -> List[Recipe]:
#         """Search recipes based on available ingredients"""
#         available_ingredients = [ing.lower().strip() for ing in available_ingredients]
#         matching_recipes = []
        
#         for recipe in self.recipes_db:
#             recipe_ingredients = [ing.lower() for ing in recipe.ingredients]
            
#             # Check how many ingredients match
#             matches = 0
#             for available in available_ingredients:
#                 for recipe_ing in recipe_ingredients:
#                     if available in recipe_ing or recipe_ing in available:
#                         matches += 1
#                         break
            
#             # If at least 30% of ingredients match, include the recipe
#             if matches >= len(recipe.ingredients) * 0.3:
#                 matching_recipes.append((recipe, matches))
        
#         # Sort by number of matches (descending)
#         matching_recipes.sort(key=lambda x: x[1], reverse=True)
#         return [recipe for recipe, _ in matching_recipes]
    
#     def filter_recipes(self, cuisine: str = None, difficulty: str = None, 
#                       category: str = None, max_time: int = None) -> List[Recipe]:
#         """Filter recipes based on criteria"""
#         filtered_recipes = self.recipes_db.copy()
        
#         if cuisine and cuisine != "All":
#             filtered_recipes = [r for r in filtered_recipes if r.cuisine.lower() == cuisine.lower()]
        
#         if difficulty and difficulty != "All":
#             filtered_recipes = [r for r in filtered_recipes if r.difficulty.lower() == difficulty.lower()]
        
#         if category and category != "All":
#             filtered_recipes = [r for r in filtered_recipes if r.category.lower() == category.lower()]
        
#         if max_time:
#             filtered_recipes = [r for r in filtered_recipes if (r.prep_time + r.cook_time) <= max_time]
        
#         return filtered_recipes
    
#     def get_random_recipe(self) -> Recipe:
#         """Get a random recipe"""
#         return random.choice(self.recipes_db)
    
#     def generate_shopping_list(self, recipe: Recipe) -> List[str]:
#         """Generate shopping list from recipe"""
#         shopping_list = []
#         for ingredient in recipe.ingredients:
#             # Clean up ingredient (remove measurements)
#             clean_ingredient = re.sub(r'^\d+(\.\d+)?\s*(cups?|tbsp|tsp|lbs?|oz|g|kg|ml|l)?\s*', '', ingredient)
#             clean_ingredient = re.sub(r',.*$', '', clean_ingredient)  # Remove everything after comma
#             shopping_list.append(clean_ingredient.strip())
        
#         return shopping_list

# # Initialize the recipe generator
# @st.cache_resource
# def get_recipe_generator():
#     return RecipeGenerator()

# # Streamlit App Configuration
# st.set_page_config(
#     page_title="Recipe Generator",
#     page_icon="🍳",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS
# st.markdown("""
# <style>
#     .recipe-card {
#         background-color: #f8f9fa;
#         padding: 20px;
#         border-radius: 10px;
#         border-left: 5px solid #ff6b6b;
#         margin: 10px 0;
#     }
#     .recipe-title {
#         color: #2c3e50;
#         font-size: 24px;
#         font-weight: bold;
#         margin-bottom: 10px;
#     }
#     .recipe-meta {
#         color: #7f8c8d;
#         font-size: 14px;
#         margin-bottom: 15px;
#     }
#     .ingredient-list {
#         background: linear-gradient(135deg, #ff6b6b, #ffa500, #32cd32, #1e90ff);
#         background-size: 400% 400%;
#         animation: gradientShift 3s ease infinite;
#         color: white;
#         font-weight: bold;
#         text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
#         padding: 20px;
#         border-radius: 10px;
#         margin: 10px 0;
#         border: 3px solid #fff;
#         box-shadow: 0 4px 15px rgba(0,0,0,0.2);
#     }
    
#     @keyframes gradientShift {
#         0% { background-position: 0% 50%; }
#         50% { background-position: 100% 50%; }
#         100% { background-position: 0% 50%; }
#     }
#     .instruction-step {
#         margin: 8px 0;
#         padding: 8px;
#         background-color: black;
#         border-radius: 5px;
#         border-left: 3px solid #3498db;
#     }
#     .stButton > button {
#         background-color: #ff6b6b;
#         color: white;
#         border: none;
#         border-radius: 5px;
#         padding: 10px 20px;
#         font-weight: bold;
#     }
#     .stButton > button:hover {
#         background-color: #ff5252;
#     }
# </style>
# """, unsafe_allow_html=True)

# def main():
#     # Initialize recipe generator
#     recipe_gen = get_recipe_generator()
    
#     # Header
#     st.title("🍳 Recipe Generator")
#     st.markdown("---")
    
#     # Sidebar
#     st.sidebar.title("Recipe Options")
    
#     # Mode selection
#     mode = st.sidebar.selectbox(
#         "Choose Mode",
#         ["Browse All Recipes", "Search by Ingredients", "Filter Recipes", "Random Recipe"]
#     )
    
#     if mode == "Browse All Recipes":
#         st.header("All Available Recipes")
        
#         for recipe in recipe_gen.recipes_db:
#             display_recipe(recipe)
    
#     elif mode == "Search by Ingredients":
#         st.header("🔍 Find Recipes by Ingredients")
        
#         # Ingredient input
#         st.subheader("What ingredients do you have?")
#         ingredients_input = st.text_area(
#             "Enter ingredients (one per line or separated by commas):",
#             placeholder="chicken\nrice\nonion\ngarlic"
#         )
        
#         if st.button("Search Recipes"):
#             if ingredients_input:
#                 # Parse ingredients
#                 ingredients = []
#                 if ',' in ingredients_input:
#                     ingredients = [ing.strip() for ing in ingredients_input.split(',')]
#                 else:
#                     ingredients = [ing.strip() for ing in ingredients_input.split('\n') if ing.strip()]
                
#                 # Search recipes
#                 matching_recipes = recipe_gen.search_by_ingredients(ingredients)
                
#                 if matching_recipes:
#                     st.success(f"Found {len(matching_recipes)} matching recipes!")
#                     for recipe in matching_recipes:
#                         display_recipe(recipe)
#                 else:
#                     st.warning("No recipes found with those ingredients. Try different ingredients!")
#             else:
#                 st.error("Please enter some ingredients first.")
    
#     elif mode == "Filter Recipes":
#         st.header("🎯 Filter Recipes")
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             cuisine_filter = st.selectbox(
#                 "Cuisine Type",
#                 ["All", "Italian", "Asian", "American", "Mexican"]
#             )
            
#             difficulty_filter = st.selectbox(
#                 "Difficulty Level",
#                 ["All", "Easy", "Medium", "Hard"]
#             )
        
#         with col2:
#             category_filter = st.selectbox(
#                 "Category",
#                 ["All", "Main Course", "Pasta", "Salad", "Dessert"]
#             )
            
#             max_time = st.slider(
#                 "Maximum Total Time (minutes)",
#                 min_value=0,
#                 max_value=120,
#                 value=60,
#                 step=5
#             )
        
#         if st.button("Apply Filters"):
#             filtered_recipes = recipe_gen.filter_recipes(
#                 cuisine=cuisine_filter,
#                 difficulty=difficulty_filter,
#                 category=category_filter,
#                 max_time=max_time if max_time > 0 else None
#             )
            
#             if filtered_recipes:
#                 st.success(f"Found {len(filtered_recipes)} recipes matching your criteria!")
#                 for recipe in filtered_recipes:
#                     display_recipe(recipe)
#             else:
#                 st.warning("No recipes match your filters. Try adjusting your criteria.")
    
#     elif mode == "Random Recipe":
#         st.header("🎲 Random Recipe Generator")
        
#         if st.button("Generate Random Recipe", key="random_btn"):
#             random_recipe = recipe_gen.get_random_recipe()
#             st.success("Here's a random recipe for you!")
#             display_recipe(random_recipe)

# def display_recipe(recipe: Recipe):
#     """Display a recipe in a formatted card"""
    
#     with st.container():
#         # Recipe card HTML
#         st.markdown(f"""
#         <div class="recipe-card">
#             <div class="recipe-title">{recipe.name}</div>
#             <div class="recipe-meta">
#                 🍽️ Serves: {recipe.servings} | 
#                 ⏱️ Prep: {recipe.prep_time}min | 
#                 🔥 Cook: {recipe.cook_time}min | 
#                 📊 Difficulty: {recipe.difficulty} | 
#                 🌍 Cuisine: {recipe.cuisine}
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         col1, col2 = st.columns([1, 1])
        
#         with col1:
#             st.subheader("📝 Ingredients")
#             ingredients_html = "<div class='ingredient-list'>"
#             for ingredient in recipe.ingredients:
#                 ingredients_html += f"• {ingredient}<br>"
#             ingredients_html += "</div>"
#             st.markdown(ingredients_html, unsafe_allow_html=True)
        
#         with col2:
#             st.subheader("👨‍🍳 Instructions")
#             for i, instruction in enumerate(recipe.instructions, 1):
#                 st.markdown(f"""
#                 <div class="instruction-step">
#                     <strong>Step {i}:</strong> {instruction}
#                 </div>
#                 """, unsafe_allow_html=True)
        
#         # Shopping list generator
#         if st.button(f"Generate Shopping List for {recipe.name}", key=f"shopping_{recipe.name}"):
#             shopping_list = get_recipe_generator().generate_shopping_list(recipe)
            
#             st.subheader("🛒 Shopping List")
#             shopping_list_text = "\n".join([f"• {item}" for item in shopping_list])
#             st.text_area(
#                 "Copy this shopping list:",
#                 value=shopping_list_text,
#                 height=150,
#                 key=f"shopping_text_{recipe.name}"
#             )
        
#         st.markdown("---")

# if __name__ == "__main__":
#     main()

from flask import Flask, render_template, request, jsonify, session
import google.generativeai as genai
import json
import re
from datetime import datetime
import os
from typing import List, Dict, Any

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key

# Set up Google Gemini AI API Key
genai.configure(api_key="your-actual-api-key-here")  # Replace with your actual API key

class RecipeDatabase:
    def __init__(self):
        self.recipes = self.load_recipes()
        self.user_favorites = {}  # In production, use a proper database
    
    def load_recipes(self):
        """Load existing recipes from file or initialize with defaults"""
        default_recipes = [
            {
                "name": "Classic Spaghetti Carbonara",
                "ingredients": ["400g spaghetti", "200g pancetta", "4 eggs", "100g Pecorino Romano", "garlic", "black pepper"],
                "cuisine": "Italian",
                "difficulty": "Medium",
                "prep_time": 15,
                "cook_time": 20,
                "servings": 4,
                "rating": 4.5,
                "tags": ["pasta", "quick", "traditional"]
            },
            {
                "name": "Chicken Stir Fry",
                "ingredients": ["chicken breast", "bell peppers", "onion", "soy sauce", "garlic", "ginger"],
                "cuisine": "Asian",
                "difficulty": "Easy",
                "prep_time": 15,
                "cook_time": 10,
                "servings": 4,
                "rating": 4.3,
                "tags": ["healthy", "quick", "protein"]
            }
        ]
        return default_recipes
    
    def add_recipe(self, recipe_data):
        """Add a new recipe to the database"""
        recipe_data['id'] = len(self.recipes) + 1
        recipe_data['created_at'] = datetime.now().isoformat()
        recipe_data['rating'] = 0
        self.recipes.append(recipe_data)
        return recipe_data
    
    def search_recipes(self, query, filters=None):
        """Search recipes based on ingredients or name"""
        results = []
        query_lower = query.lower()
        
        for recipe in self.recipes:
            # Search in name and ingredients
            if (query_lower in recipe['name'].lower() or 
                any(query_lower in ing.lower() for ing in recipe['ingredients'])):
                
                if filters:
                    if (filters.get('cuisine') and filters['cuisine'] != recipe.get('cuisine')):
                        continue
                    if (filters.get('difficulty') and filters['difficulty'] != recipe.get('difficulty')):
                        continue
                    if (filters.get('max_time') and 
                        (recipe.get('prep_time', 0) + recipe.get('cook_time', 0)) > filters['max_time']):
                        continue
                
                results.append(recipe)
        
        return sorted(results, key=lambda x: x.get('rating', 0), reverse=True)

# Initialize database
recipe_db = RecipeDatabase()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/browse')
def browse():
    return render_template("browse.html")

@app.route('/favorites')
def favorites():
    return render_template("favorites.html")

@app.route('/api/recipes')
def get_recipes():
    """API endpoint to get all recipes with optional filtering"""
    cuisine = request.args.get('cuisine', '')
    difficulty = request.args.get('difficulty', '')
    max_time = request.args.get('max_time', type=int)
    
    filters = {}
    if cuisine and cuisine != 'all':
        filters['cuisine'] = cuisine
    if difficulty and difficulty != 'all':
        filters['difficulty'] = difficulty
    if max_time:
        filters['max_time'] = max_time
    
    if filters:
        recipes = recipe_db.search_recipes('', filters)
    else:
        recipes = recipe_db.recipes
    
    return jsonify({"recipes": recipes})

@app.route('/api/search')
def search_recipes():
    """API endpoint for recipe search"""
    query = request.args.get('q', '')
    cuisine = request.args.get('cuisine', '')
    difficulty = request.args.get('difficulty', '')
    max_time = request.args.get('max_time', type=int)
    
    filters = {}
    if cuisine and cuisine != 'all':
        filters['cuisine'] = cuisine
    if difficulty and difficulty != 'all':
        filters['difficulty'] = difficulty
    if max_time:
        filters['max_time'] = max_time
    
    results = recipe_db.search_recipes(query, filters)
    return jsonify({"recipes": results})

@app.route('/generate_recipe', methods=['POST'])
def generate_recipe():
    data = request.json
    recipe_name = data.get('recipe_name', '').strip()
    ingredients = data.get('ingredients', '').strip()
    diet = data.get('diet', 'any')
    cuisine = data.get('cuisine', '')
    difficulty = data.get('difficulty', 'medium')
    servings = data.get('servings', 4)

    if not recipe_name or not ingredients:
        return jsonify({"error": "Please enter a recipe name and ingredients."}), 400

    # Enhanced prompt for better AI generation
    prompt = f"""
    Create a detailed {diet} recipe for {recipe_name} using these ingredients: {ingredients}.
    
    Requirements:
    - Cuisine style: {cuisine if cuisine else 'any'}
    - Difficulty level: {difficulty}
    - Servings: {servings}
    - Include prep time and cook time
    - Provide step-by-step instructions
    - Include nutritional tips if applicable
    - Suggest variations or substitutions
    
    Format the response with clear sections:
    - Recipe Name
    - Prep Time & Cook Time
    - Servings
    - Ingredients (with exact measurements)
    - Instructions (numbered steps)
    - Tips & Variations
    - Nutritional Information (if relevant)
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        
        # Parse and structure the AI response
        recipe_text = response.text
        
        # Extract structured data from AI response
        recipe_data = parse_ai_recipe(recipe_text, {
            'name': recipe_name,
            'ingredients_input': ingredients,
            'diet': diet,
            'cuisine': cuisine,
            'difficulty': difficulty,
            'servings': servings
        })
        
        # Save the generated recipe
        saved_recipe = recipe_db.add_recipe(recipe_data)
        
        return jsonify({
            "recipe": recipe_text,
            "structured_data": saved_recipe,
            "success": True
        })

    except Exception as e:
        return jsonify({"error": f"AI service error: {str(e)}"}), 500

def parse_ai_recipe(ai_text, metadata):
    """Parse AI-generated recipe text into structured data"""
    
    # Extract prep time
    prep_time_match = re.search(r'prep time[:\s]*(\d+)', ai_text, re.IGNORECASE)
    prep_time = int(prep_time_match.group(1)) if prep_time_match else 30
    
    # Extract cook time
    cook_time_match = re.search(r'cook time[:\s]*(\d+)', ai_text, re.IGNORECASE)
    cook_time = int(cook_time_match.group(1)) if cook_time_match else 30
    
    # Extract ingredients list
    ingredients = []
    ingredients_section = re.search(r'ingredients[:\s]*\n(.*?)(?=\n[A-Z]|\nInstructions|\nSteps|$)', 
                                   ai_text, re.IGNORECASE | re.DOTALL)
    if ingredients_section:
        ingredient_lines = ingredients_section.group(1).strip().split('\n')
        ingredients = [line.strip('- •*').strip() for line in ingredient_lines if line.strip()]
    
    return {
        'name': metadata['name'],
        'ingredients': ingredients if ingredients else metadata['ingredients_input'].split(','),
        'cuisine': metadata['cuisine'] or 'International',
        'difficulty': metadata['difficulty'].title(),
        'prep_time': prep_time,
        'cook_time': cook_time,
        'servings': metadata['servings'],
        'diet_type': metadata['diet'],
        'full_recipe': ai_text,
        'tags': generate_tags(metadata, ai_text)
    }

def generate_tags(metadata, recipe_text):
    """Generate relevant tags for the recipe"""
    tags = []
    
    # Add diet-based tags
    if metadata['diet'] != 'any':
        tags.append(metadata['diet'])
    
    # Add cuisine tag
    if metadata['cuisine']:
        tags.append(metadata['cuisine'].lower())
    
    # Add difficulty tag
    tags.append(metadata['difficulty'].lower())
    
    # Add time-based tags
    total_time = 60  # default
    if 'quick' in recipe_text.lower() or total_time <= 30:
        tags.append('quick')
    elif total_time <= 60:
        tags.append('moderate-time')
    else:
        tags.append('long-cooking')
    
    # Add ingredient-based tags
    text_lower = recipe_text.lower()
    if any(word in text_lower for word in ['chicken', 'beef', 'pork', 'fish']):
        tags.append('protein')
    if any(word in text_lower for word in ['healthy', 'nutritious', 'low-fat']):
        tags.append('healthy')
    if any(word in text_lower for word in ['spicy', 'hot', 'chili']):
        tags.append('spicy')
    
    return list(set(tags))  # Remove duplicates

@app.route('/save_favorite', methods=['POST'])
def save_favorite():
    """Save a recipe to user's favorites"""
    data = request.json
    recipe_id = data.get('recipe_id')
    
    if 'favorites' not in session:
        session['favorites'] = []
    
    if recipe_id not in session['favorites']:
        session['favorites'].append(recipe_id)
        return jsonify({"success": True, "message": "Recipe added to favorites!"})
    else:
        return jsonify({"success": False, "message": "Recipe already in favorites!"})

@app.route('/remove_favorite', methods=['POST'])
def remove_favorite():
    """Remove a recipe from user's favorites"""
    data = request.json
    recipe_id = data.get('recipe_id')
    
    if 'favorites' in session and recipe_id in session['favorites']:
        session['favorites'].remove(recipe_id)
        return jsonify({"success": True, "message": "Recipe removed from favorites!"})
    else:
        return jsonify({"success": False, "message": "Recipe not in favorites!"})

@app.route('/get_favorites')
def get_favorites():
    """Get user's favorite recipes"""
    favorite_ids = session.get('favorites', [])
    favorite_recipes = [recipe for recipe in recipe_db.recipes 
                       if recipe.get('id') in favorite_ids]
    return jsonify({"favorites": favorite_recipes})

@app.route('/rate_recipe', methods=['POST'])
def rate_recipe():
    """Rate a recipe"""
    data = request.json
    recipe_id = data.get('recipe_id')
    rating = data.get('rating', 0)
    
    if not (1 <= rating <= 5):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400
    
    # Find and update recipe rating
    for recipe in recipe_db.recipes:
        if recipe.get('id') == recipe_id:
            # Simple rating update (in production, calculate average)
            recipe['rating'] = rating
            return jsonify({"success": True, "message": "Recipe rated successfully!"})
    
    return jsonify({"error": "Recipe not found"}), 404

@app.route('/nutrition_info/<int:recipe_id>')
def get_nutrition_info(recipe_id):
    """Get nutrition information for a recipe (mock data)"""
    # In a real app, integrate with nutrition API
    nutrition = {
        "calories": 450,
        "protein": "25g",
        "carbs": "35g",
        "fat": "18g",
        "fiber": "4g",
        "sodium": "680mg"
    }
    return jsonify({"nutrition": nutrition})

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error="Internal server error"), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)