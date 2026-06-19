# ==========================================
# Codeaura Python Course: 01_what_is_vector_db.py
# ==========================================
# Concept: Vector Databases (AI Database)
# Real Life Example: Normal database 'keywords' dhoondta hai (e.g. "Red Fruit").
# Vector database 'meaning' dhoondta hai. Agar aap "Red Fruit" search karenge to ye "Apple" dikhayega,
# chahe "Apple" shabd ke paas "Red" ya "Fruit" likha bhi na ho! Ye AI ka dimaag hai.

print("--- Welcome to Vector Databases (ChromaDB Concept) ---")

print("\n1. Traditional Search (SQL):")
print("User Searches: 'Red Fruit'")
print("Database Logic: Do I have the exact words 'Red' and 'Fruit'? No. -> Result: NOT FOUND")

print("\n2. AI Search (Vector Database):")
print("User Searches: 'Red Fruit'")
print("Database Logic: 'Red Fruit' ka matlab ek aisi cheez jo lal ho aur khane wali ho.")
print("Machine converts meaning into numbers (Vectors): [0.8, 0.9, 0.1]")
print("Result: 'Apple' (Because Apple's meaning numbers are very close to [0.8, 0.9, 0.1]) -> Result: FOUND APPLE! 🍎")

print("\nVector Databases like ChromaDB and Pinecone are the secret behind ChatGPT's memory!")
print("They store 'Ideas' and 'Meanings', not just raw text.")
