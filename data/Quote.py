from random import choice
from requests import get, codes


class QuotesHandler:
    def __init__(self, api_key, categories):
        self.api_key = api_key
        self.categories = categories
        self.api_url = 'https://api.api-ninjas.com/v1/quotes'


    def generate(self):
        selected_category = choice(self.categories)

        try:
            response = get(
                f"{self.api_url}?category={selected_category}",
                headers={'X-Api-Key': self.api_key}
            )

            if response.status_code == codes.ok:
                try:
                    data = response.json()
                    if data:
                        quote = data[0].get('quote')
                        author = data[0].get('author')
                        return f"✨ «{quote}» ~ {author} 🌟"
                    else:
                        return "🚫 No quote found in the response."
                except ValueError:
                    return "❌ Error parsing response JSON."
            else:
                return f"⚠️ Error: Received status code {response.status_code}"

        except Exception as e:
            return f"🛑 An error occurred: {str(e)}"
