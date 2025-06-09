import streamlit as st
import plotly.express as px
from utils import load_data, tampilkan_gambar_resep
from config import BASE_URL
import css_styles  # Memasukkan file CSS eksternal

# =================== Set Page Config ===================
st.set_page_config(page_title="🍛 Delidish Nusantara", layout="wide", page_icon="🍛")

# =================== Memasukkan CSS dari file eksternal ===================
st.markdown(css_styles.css_code, unsafe_allow_html=True) 

# =================== Load Data ===================
df = load_data()

# =================== Sidebar ===================
st.sidebar.markdown("<div class='sidebar-header'>🍽️ Menu Navigasi</div>", unsafe_allow_html=True)
menu = st.sidebar.radio("", ["🏠 Home", "🔍 Rekomendasi", "📊 Visualisasi", "ℹ️ Tentang"])

st.sidebar.markdown("<hr style='border-color: #667eea; margin: 30px 0;'>", unsafe_allow_html=True)

# Sidebar Stats
st.sidebar.markdown("<div style='color: #ecf0f1; text-align: center; margin-bottom: 20px;'>", unsafe_allow_html=True)
st.sidebar.metric("Total Resep", f"{len(df):,}")
st.sidebar.metric("Kategori", f"{df['Category'].nunique()}")
st.sidebar.markdown("</div>", unsafe_allow_html=True)

st.sidebar.markdown(
    "<div style='color: #bdc3c7; text-align: center; margin-top: 40px;'>©️ Telkom University 2025</div>",
    unsafe_allow_html=True
)

# =================== Menu Konten Berdasarkan Pilihan ===================
if menu == "🏠 Home":
    # Hero Section
    st.markdown("""<div class='main-header floating'><h1 class='glowing'>🍛 Delidish Nusantara</h1><p>Jelajahi Beragam Cita Rasa dan Temukan Makanan Sesuai Preferensimu</p></div>""", unsafe_allow_html=True)

    # Feature Cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class='stat-card'>
                <div style='font-size: 3rem; margin-bottom: 15px;'>🔍</div>
                <div class='stat-number'>Smart</div>
                <div class='stat-label'>Pencarian Cerdas</div>
                <p style='margin-top: 15px; color: #666;'>Temukan makanan berdasarkan bahan, rasa, dan preferensi diet Anda</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class='stat-card'>
                <div style='font-size: 3rem; margin-bottom: 15px;'>📊</div>
                <div class='stat-number'>Visual</div>
                <div class='stat-label'>Analisis Mendalam</div>
                <p style='margin-top: 15px; color: #666;'>Statistik dan visualisasi interaktif tentang kuliner Nusantara</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class='stat-card'>
                <div style='font-size: 3rem; margin-bottom: 15px;'>🍽️</div>
                <div class='stat-number'>Fresh</div>
                <div class='stat-label'>Resep Terkini</div>
                <p style='margin-top: 15px; color: #666;'>Database resep yang selalu diperbarui dari komunitas</p>
            </div>
        """, unsafe_allow_html=True)

    # Popular Dishes Preview
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center; margin: 40px 0;'>
            <h2 style='color: white; font-weight: 600;'>🌟 Makanan Terpopuler Hari Ini</h2>
        </div>
    """, unsafe_allow_html=True)

    popular_dishes = df.nlargest(3, 'Loves')
    cols = st.columns(3)
    for idx, (_, dish) in enumerate(popular_dishes.iterrows()):
        with cols[idx]:
            tampilkan_gambar_resep(dish['URL'], dish['Title Cleaned'], dish['Category'])
            
            # Menampilkan detail makanan
            st.markdown(f"""
                <div class='food-card' style='flex-direction: column; text-align: center; padding: 30px;'>
                    <h3 style='color: #2c3e50; margin-bottom: 10px;'>{dish['Title Cleaned']}</h3>
                    <div class='meta-tag' style='margin: 10px auto; display: inline-block;'>
                        ❤️ {dish['Loves']} likes
                    </div>
                    <p style='color: #666; margin-top: 15px;'>{dish['Category']}</p>
                </div>
            """, unsafe_allow_html=True)

elif menu == "🔍 Rekomendasi":
    st.markdown("""
        <div class='main-header'>
            <h1>🔍 Pencarian & Rekomendasi</h1>
            <p>Temukan makanan impian Anda dengan filter canggih</p>
        </div>
    """, unsafe_allow_html=True)

    query = st.text_input("", placeholder="Cari makanan (contoh: ayam, diet, pedas)", key="search")

    col1, col2 = st.columns(2)
    with col1:
        kategori_list = ['Semua'] + sorted(df['Category'].unique().tolist())
        kategori = st.selectbox("📦 Kategori", kategori_list)
    with col2:
        sort_by = st.selectbox("🔄 Urutkan berdasarkan", ["Popularitas", "Nama", "Kategori"])

    st.markdown("""
        <div class='filter-card'>
            <h3>🎯 Filter Preferensi</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 10px;">
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        is_vegan = st.checkbox("🍧 Manis")
    with col2:
        prefer_pedas = st.checkbox("🌶️ Pedas")
    with col3:
        prefer_diet = st.checkbox("⚖️ Cocok untuk Diet")
    with col4:
        prefer_naik_bb = st.checkbox("🍗 Naik Berat Badan")

    # Apply Filters
    filtered_df = df.copy()

    if query:
        filtered_df = filtered_df[
            filtered_df['Title Cleaned'].str.contains(query, case=False, na=False)
        ]

    if kategori != 'Semua':
        filtered_df = filtered_df[filtered_df['Category'] == kategori]

    if is_vegan:
        filtered_df = filtered_df[filtered_df["manis"] == 1]
    if prefer_pedas:
        filtered_df = filtered_df[filtered_df["pedas"] == 1]
    if prefer_diet:
        filtered_df = filtered_df[filtered_df["cocok_diet"] == 1]
    if prefer_naik_bb:
        filtered_df = filtered_df[filtered_df["cocok_naik_berat"] == 1]

    # Sort results
    if sort_by == "Popularitas":
        filtered_df = filtered_df.sort_values(by='Loves', ascending=False)
    elif sort_by == "Nama":
        filtered_df = filtered_df.sort_values(by='Title Cleaned')
    else:  # Kategori
        filtered_df = filtered_df.sort_values(by='Category')

    # Results
    st.markdown(f"""
        <div class='results-header'>
            🎉 Ditemukan {filtered_df.shape[0]} makanan yang sesuai dengan kriteria Anda!
        </div>
    """, unsafe_allow_html=True)

    if filtered_df.empty:
        st.markdown("""
            <div style='text-align: center; padding: 60px; background: rgba(255,255,255,0.15); border-radius: 25px; color: white; backdrop-filter: blur(15px);'>
                <h3>😔 Oops! Tidak ada makanan yang sesuai</h3>
                <p>Coba ubah filter pencarian Anda</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        top_makanan = filtered_df.head(10)
        
        # Progress bar for loading images
        if len(top_makanan) > 0:
            progress_bar = st.progress(0)
            status_text = st.empty()
            
        for idx, (_, row) in enumerate(top_makanan.iterrows()):
            # Update progress
            progress = (idx + 1) / len(top_makanan)
            progress_bar.progress(progress)
            status_text.text(f'Memuat gambar... {idx + 1}/{len(top_makanan)}')
            
            emoji_map = {'Makanan Utama': '🍛', 'Makanan Ringan': '🍪', 'Minuman': '🥤', 'Dessert': '🍰', 'Kuah/Sup': '🍲'}
            emoji = emoji_map.get(row['Category'], '🍽️')
            
            # Build flavor tags
            flavor_tags = []
            if row['pedas']: flavor_tags.append('<span class="flavor-tag">🌶️ Pedas</span>')
            if row['manis']: flavor_tags.append('<span class="flavor-tag">🍯 Manis</span>')
            if row['gurih']: flavor_tags.append('<span class="flavor-tag">🧂 Gurih</span>')
            if row['asam']: flavor_tags.append('<span class="flavor-tag">🍋 Asam</span>')
            flavor_html = ' '.join(flavor_tags[:3]) if flavor_tags else '<span class="flavor-tag">⚖️ Rasa Seimbang</span>'

            # Extract image from Cookpad
            with st.container():
                col_kiri, col_kanan = st.columns([2, 1])  # kiri lebih lebar

                with col_kiri:
                    st.markdown(f"""
                        <div style="background-color: white; padding: 15px; border-radius: 8px;">
                            <div class='food-title'>{emoji} {row['Title Cleaned']}</div>
                            <div class='food-meta'>
                                <div class='meta-tag'>📂 {row['Category']}</div>
                                <div class='meta-tag'>❤️ {int(row['Loves'])} likes</div>
                                {flavor_html}
                            </div>
                            <div class='food-ingredients'>
                                <strong>🥘 Bahan Utama:</strong><br>
                                {' '.join(row['Ingredients Cleaned'].split()[:12])}...
                            </div>
                            <a href="{row['URL']}" class='food-link' target="_blank">📖 Lihat Resep Lengkap di Cookpad</a>
                        </div>
                    """, unsafe_allow_html=True)

                with col_kanan:
                    tampilkan_gambar_resep(row['URL'], row['Title Cleaned'], row['Category'])

            # Detailed recipe expander
            with st.expander("👩‍🍳 Detail Resep Lengkap", expanded=False):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**📝 Bahan Lengkap:**\n\n{row['Ingredients Cleaned']}")
                with col2:
                    st.markdown(f"**🔥 Langkah Memasak:**\n\n{row['Steps']}")
        
        # Clear progress bar
        if len(top_makanan) > 0:
            progress_bar.empty()
            status_text.empty()

elif menu == "📊 Visualisasi":
    st.markdown("""
        <div class='main-header'>
            <h1>📊 Dashboard Analytics</h1>
            <p>Jelajahi tren dan statistik kuliner</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
            <div class='stat-card'>
                <div class='stat-number'>{len(df):,}</div>
                <div class='stat-label'>Total Resep</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div class='stat-card'>
                <div class='stat-number'>{df['Category'].nunique()}</div>
                <div class='stat-label'>Kategori</div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
            <div class='stat-card'>
                <div class='stat-number'>{df['Loves'].sum():,}</div>
                <div class='stat-label'>Total Likes</div>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        avg_likes = df['Loves'].mean()
        st.markdown(f"""
            <div class='stat-card'>
                <div class='stat-number'>{avg_likes:.0f}</div>
                <div class='stat-label'>Rata-rata Likes</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    
    # Visualisasi untuk Distribusi Kategori Makanan
    with col1:
        st.markdown("""
            <div class='stat-card-big'>
                <h3>🍱 Distribusi Kategori Makanan</h3>
        """, unsafe_allow_html=True)
        kategori_counts = df['Category'].value_counts()
        fig = px.pie(
            values=kategori_counts.values,
            names=kategori_counts.index,
            color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='black'))
        # Wrap the plot in the div for stat-card-big
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Visualisasi untuk Profil Rasa Populer
    with col2:
        st.markdown("""
            <div class='stat-card-big'>
                <h3>🌶️ Profil Rasa Populer</h3>
        """, unsafe_allow_html=True)
        rasa_cols = ['pedas', 'manis', 'asin', 'asam', 'gurih']
        rasa_counts = df[rasa_cols].sum().sort_values(ascending=True)
        fig = px.bar(
            x=rasa_counts.values,
            y=rasa_counts.index,
            orientation='h',
            color=rasa_counts.values,
            color_continuous_scale='Viridis')
        fig.update_layout(
            xaxis_title='Kategori Makanan',
            yaxis_title='Jumlah Likes',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='black'),
            showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Visualisasi untuk Tren Popularitas vs Kategori
    st.markdown("""
        <div class='stat-card-big'>
            <h3>📈 Tren Popularitas vs Kategori</h3>
    """, unsafe_allow_html=True)
    fig = px.scatter(
        df,
        x='Category',
        y='Loves',
        color='Category',
        size='Loves',
        hover_data=['Title Cleaned'],
        color_discrete_sequence=px.colors.qualitative.Vivid)
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='black'))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

else:  # Tentang
    st.markdown("""
        <div class='main-header'>
            <h1>ℹ️ Tentang Delidish Nusantara</h1>
            <p>Platform rekomendasi kuliner pintar berbasis preferensi pengguna</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Misi
    st.markdown("""
        <div class='about-card'>
            <h2>🎯 Misi Kami</h2>
            <p style='font-size: 1.1rem; line-height: 1.8; color: #555;'>
                Delidish hadir untuk membantu pengguna menemukan makanan favorit berdasarkan cita rasa,
                kebutuhan diet, dan bahan yang tersedia. Dengan memanfaatkan teknologi pembelajaran mesin,
                kami memperkenalkan cara baru untuk menjelajahi dunia kuliner secara personal dan menyenangkan.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Tim Developer
    st.markdown("""
        <div class='about-card'>
            <h2>👥 Tim Pengembang</h2>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class='team-member'>
                <div style='font-size: 3rem;'>👩‍💻</div>
                <h4>Chacha Alisha Dewintasari</h4>
                <p>1305220036</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class='team-member'>
                <div style='font-size: 3rem;'>👩‍🔬</div>
                <h4>Yusry Anandita Yulianti</h4>
                <p>1305220037</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class='team-member'>
                <div style='font-size: 3rem;'>👨‍💼</div>
                <h4>Bima Harish Mazaya</h4>
                <p>1305220038</p>
            </div>
        """, unsafe_allow_html=True)

    # Teknologi
    st.markdown("""
        <div class='about-card'>
            <h2>🛠️ Teknologi yang Digunakan</h2>
            <div class='tech-stack-grid'>
                <div class='tech-box' style='background: linear-gradient(135deg, #667eea, #764ba2);'>
                    <h4>Frontend</h4>
                    <p>Streamlit, HTML/CSS</p>
                </div>
                <div class='tech-box' style='background: linear-gradient(135deg, #f093fb, #f5576c);'>
                    <h4>Data Processing</h4>
                    <p>Pandas, NumPy, Scikit-learn</p>
                </div>
                <div class='tech-box' style='background: linear-gradient(135deg, #4facfe, #00f2fe);'>
                    <h4>Visualisasi</h4>
                    <p>Plotly, Matplotlib</p>
                </div>
                <div class='tech-box' style='background: linear-gradient(135deg, #43e97b, #38f9d7);'>
                    <h4>Machine Learning</h4>
                    <p>TF-IDF, Content-Based Recommender</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <div style='text-align: center; margin-top: 50px; padding: 30px; background: rgba(255,255,255,0.1); border-radius: 20px; color: white;'>
            <h3 style='margin-bottom: 15px;'>🏛️ Telkom University</h3>
            <p style='font-size: 1.1rem;'>Fakultas Informatika • Tahun 2025</p>
        </div>
    """, unsafe_allow_html=True)