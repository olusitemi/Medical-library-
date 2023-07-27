class MedicalLibrary:
    def __init__(self):
        self.library = {}
        self.categories = {}

    def add_article(self, title, content, category=None):
        if title in self.library:
            print("An article with the same title already exists. Use a different title.")
        else:
            self.library[title] = {"content": content, "category": category}
            print("Article added successfully.")

    def search_article(self, keyword):
        results = {}
        for title, article_data in self.library.items():
            if keyword.lower() in article_data["content"].lower() or keyword.lower() in title.lower():
                results[title] = article_data
        return results

    def view_article(self, title):
        if title in self.library:
            article_data = self.library[title]
            print(f"Title: {title}\nCategory: {article_data['category']}\n")
            print(article_data["content"])
        else:
            print("Article not found.")

    def modify_article(self, title, new_content):
        if title in self.library:
            self.library[title]["content"] = new_content
            print("Article modified successfully.")
        else:
            print("Article not found.")

    def delete_article(self, title):
        if title in self.library:
            del self.library[title]
            print("Article deleted successfully.")
        else:
            print("Article not found.")

    def add_category(self, category_name):
        if category_name in self.categories:
            print("Category already exists.")
        else:
            self.categories[category_name] = []
            print(f"Category '{category_name}' added successfully.")

    def assign_article_to_category(self, title, category):
        if title in self.library:
            if category in self.categories:
                self.library[title]["category"] = category
                self.categories[category].append(title)
                print(f"Article '{title}' assigned to category '{category}' successfully.")
            else:
                print(f"Category '{category}' not found.")
        else:
            print("Article not found.")

    def get_articles_by_category(self, category):
        if category in self.categories:
            category_articles = self.categories[category]
            return {title: self.library[title] for title in category_articles}
        else:
            return {}

def main():
    library = AdvancedMedicalLibrary()

    while True:
        print("\n==== Advanced Medical Digital Library ====")
        print("1. Add Article")
        print("2. Search Articles")
        print("3. View Article")
        print("4. Modify Article")
        print("5. Delete Article")
        print("6. Add Category")
        print("7. Assign Article to Category")
        print("8. Get Articles by Category")
        print("9. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")

        if choice == "1":
            title = input("Enter article title: ")
            content = input("Enter article content: ")
            category = input("Enter article category (optional): ")
            library.add_article(title, content, category)

        elif choice == "2":
            keyword = input("Enter keyword to search for articles: ")
            results = library.search_article(keyword)
            if results:
                print("\nSearch Results:")
                for title, article_data in results.items():
                    print(f"\nTitle: {title}\nCategory: {article_data['category']}\n{article_data['content']}")
            else:
                print("No matching articles found.")

        elif choice == "3":
            title = input("Enter the title of the article to view: ")
            library.view_article(title)

        elif choice == "4":
            title = input("Enter the title of the article to modify: ")
            new_content = input("Enter the new content for the article: ")
            library.modify_article(title, new_content)

        elif choice == "5":
            title = input("Enter the title of the article to delete: ")
            library.delete_article(title)

        elif choice == "6":
            category_name = input("Enter the name of the category to add: ")
            library.add_category(category_name)

        elif choice == "7":
            title = input("Enter the title of the article to assign to a category: ")
            category = input("Enter the name of the category: ")
            library.assign_article_to_category(title, category)

        elif choice == "8":
            category = input("Enter the name of the category to get articles: ")
            articles = library.get_articles_by_category(category)
            if articles:
                print(f"\nArticles in Category '{category}':")
                for title, article_data in articles.items():
                    print(f"\nTitle: {title}\nCategory: {article_data['category']}\n{article_data['content']}")
            else:
                print(f"No articles found in Category '{category}'.")

        elif choice == "9":
            print("Exiting the Advanced Medical Digital Library.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
