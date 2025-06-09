import pandas as pd
import requests
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import streamlit as st

@st.cache_data
def load_data() -> pd.DataFrame:
    try:
        df = pd.read_csv("Makanan Indonesia Final.csv")
        st.success("✅ Data berhasil dimuat.")
        return df
    except Exception as e:
        st.error(f"❌ Error loading data: {str(e)}")
        st.stop()

@st.cache_data(ttl=3600)  # Cache for 1 hour
def extract_image_from_cookpad(url):
    """Extract image URL from Cookpad recipe page"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Try multiple selectors for Cookpad images
            image_selectors = [
                'img[data-large-photo]',
                '.recipe-show__main-photo img',
                '.main-photo img',
                'img.recipe-photo',
                'meta[property="og:image"]',
                'img[src*="image.cookpad.com"]'
            ]
            
            for selector in image_selectors:
                if selector.startswith('meta'):
                    element = soup.select_one(selector)
                    if element:
                        return element.get('content')
                else:
                    element = soup.select_one(selector)
                    if element:
                        img_url = element.get('data-large-photo') or element.get('src')
                        if img_url:
                            # Convert relative URL to absolute URL
                            if img_url.startswith('//'):
                                img_url = 'https:' + img_url
                            elif img_url.startswith('/'):
                                img_url = urljoin(url, img_url)
                            return img_url
            
            # Fallback: look for any image in the content
            images = soup.find_all('img')
            for img in images:
                src = img.get('src', '')
                if 'image.cookpad.com' in src or 'recipe' in src.lower():
                    if src.startswith('//'):
                        src = 'https:' + src
                    elif src.startswith('/'):
                        src = urljoin(url, src)
                    return src
                    
    except Exception as e:
        st.warning(f"Error extracting image: {str(e)}")
    
    return None

def get_fallback_food_image(food_name, category):
    """Get fallback food image from a free API or return emoji"""
    try:
        category_emojis = {
            'Makanan Utama': '🍛',
            'Makanan Ringan': '🍪', 
            'Minuman': '🥤',
            'Dessert': '🍰',
            'Kuah/Sup': '🍲'
        }
        return category_emojis.get(category, '🍽️')
    except:
        return '🍽️'

def tampilkan_gambar_resep(url, title, category):
    img_url = extract_image_from_cookpad(url)
    if img_url:
        try:
            response = requests.get(img_url, timeout=5)
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                st.image(img, caption=None, width=600)
                return
        except:
            pass
    # Fallback emoji
    emoji_map = {
        'Makanan Utama': '🍛',
        'Makanan Ringan': '🍪',
        'Minuman': '🥤',
        'Dessert': '🍰',
        'Kuah/Sup': '🍲'
    }
    emoji = emoji_map.get(category, '🍽️')
    st.markdown(f"<div style='font-size: 4rem; text-align: center;'>{emoji}</div>", unsafe_allow_html=True)