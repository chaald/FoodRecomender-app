# =================== Enhanced CSS Styling ===================
css_code = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
        
        .stApp {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: 'Poppins', sans-serif;
        }
        
        /* Custom Card Styling */
        .food-card {
            background: linear-gradient(145deg, #ffffff 0%, #f8f9ff 100%);
            border: none;
            border-radius: 25px;
            padding: 0;
            margin-bottom: 30px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.15);
            transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
            position: relative;
            overflow: hidden;
            display: flex;
            min-height: 200px;
        }
        
        .food-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 6px;
            background: linear-gradient(90deg, #667eea, #764ba2, #667eea, #764ba2);
            background-size: 200% 100%;
            animation: shimmer 3s infinite;
        }
        
        @keyframes shimmer {
            0% { background-position: -200% 0; }
            100% { background-position: 200% 0; }
        }
        
        .food-card:hover {
            transform: translateY(-12px) scale(1.02);
            box-shadow: 0 25px 50px rgba(0,0,0,0.25);
        }
        
        .food-card-content {
            flex: 1;
            padding: 30px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        
        .food-card-image {
            width: 250px;
            height: 100%;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
        }
        
        .food-card-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.4s ease;
        }
        
        .food-card:hover .food-card-image img {
            transform: scale(1.1);
        }
        
        .food-card-image.loading {
            background: linear-gradient(45deg, #f0f2f5, #e1e8ed, #f0f2f5);
            background-size: 200% 200%;
            animation: loading 1.5s infinite;
        }
        
        @keyframes loading {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .food-title {
            color: #2c3e50;
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 12px;
            line-height: 1.3;
        }
        
        .food-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 20px;
        }
        
        .meta-tag {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 5px;
        }
        
        .flavor-tag {
            background: linear-gradient(135deg, #ffeaa7, #fdcb6e);
            color: #2d3436;
            padding: 6px 12px;
            border-radius: 15px;
            font-size: 0.8rem;
            font-weight: 500;
        }
        
        .food-ingredients {
            color: #555;
            margin-bottom: 25px;
            line-height: 1.7;
            background: linear-gradient(135deg, #f8f9fa, #e9ecef);
            padding: 20px;
            border-radius: 15px;
            border-left: 5px solid #667eea;
            font-size: 0.95rem;
        }
        
        .food-link {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white !important;
            padding: 14px 28px;
            border-radius: 25px;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-weight: 600;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            align-self: flex-start;
        }
        
        .food-link:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
            text-decoration: none;
            color: white !important;
        }
        
        /* Header Styling */
        .main-header {
            text-align: center;
            padding: 60px 0;
            background: linear-gradient(135deg, rgba(255,255,255,0.15), rgba(255,255,255,0.05));
            border-radius: 30px;
            margin-bottom: 40px;
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255,255,255,0.2);
        }
        
        .main-header h1 {
            color: white !important;
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 15px;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        }
        
        .main-header p {
            color: rgba(255,255,255,0.9) !important;
            font-size: 1.3rem;
            font-weight: 400;
        }
        
        .about-card {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            margin: 30px 0;
            border-left: 5px solid #667eea;
        }
        .about-card h2 {
            text-align: center;
            font-family: 'Arial', sans-serif;
            color: #667eea;
            margin-bottom: 15px;
        }
        .team-member {
            text-align: center;
            padding: 20px;
            background: #fff;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.05);
            margin-top: 10px;
        }
        .team-member h4 {
            margin: 10px 0 5px 0;
            font-size: 1.1rem;
            color: #000000;
        }
            
        .team-member p {
            font-size: 0.95rem;
            color: #444;
            margin: 4px 0;
            line-height: 1.5;
        }
        .tech-box {
            color: white;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
        }
        
        /* Sidebar Enhancement */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%);
        }
        
        .sidebar-header {
            color: #ecf0f1 !important;
            font-size: 1.6rem;
            font-weight: 700;
            text-align: center;
            padding: 25px 0;
            border-bottom: 3px solid #667eea;
            margin-bottom: 25px;
        }
        
        /* Filter Cards */
        .filter-card {
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(15px);
            border-radius: 16px;
            padding: 16px;
            margin-bottom: 16px;
            border: 1px solid rgba(255,255,255,0.3);
            text-align: center;
        }
        
        .filter-card h3 {
            color: white !important;
            margin-bottom: 16px;
            font-size: 1.3rem;
            font-weight: 600;
        }
        
        /* Results Header */
        .results-header {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 20px 30px;
            border-radius: 20px;
            margin-bottom: 35px;
            text-align: center;
            font-weight: 700;
            font-size: 1.2rem;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        }
        
        /* Stats Cards */
        .stat-card {
            background: linear-gradient(145deg, #ffffff, #f0f2f5);
            border-radius: 25px;
            padding: 35px;
            text-align: center;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            margin-bottom: 25px;
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
        }
        
        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #667eea, #764ba2);
        }
        
        .stat-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }
            
        /* Stat Card for Large Visualizations */
        .stat-card-big {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(15px);
            border-radius: 16px;
            padding: 30px;
            margin-bottom: 30px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            display: flex;
            flex-direction: column;
            gap: 20px;
            width: 100%;  /* Make sure it spans the full width */
        }

        .stat-card-big h3 {
            color: white !important;
            margin-bottom: 20px;
            font-size: 1.5rem;
            font-weight: 700;
            text-align: center;
        }

        .stat-card-big .plotly-figure {
            width: 100% !important;
            height: auto !important;
            margin: 0 auto;
        }
        
        .stat-number {
            font-size: 2.8rem;
            font-weight: 800;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 15px 0;
        }
        
        .stat-label {
            color: #666;
            font-weight: 600;
            font-size: 1.1rem;
        }
        
        /* Loading Spinner */
        .loading-spinner {
            border: 3px solid #f3f3f3;
            border-top: 3px solid #667eea;
            border-radius: 50%;
            width: 30px;
            height: 30px;
            animation: spin 1s linear infinite;
            margin: 20px auto;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        /* Enhanced Animations */
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-15px); }
        }
        
        .floating {
            animation: float 4s ease-in-out infinite;
        }
        
        @keyframes glow {
            0%, 100% { text-shadow: 0 0 20px rgba(255, 255, 255, 0.5); }
            50% { text-shadow: 0 0 40px rgba(255, 255, 255, 0.8); }
        }
        
        .glowing {
            animation: glow 3s infinite;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .food-card {
                flex-direction: column;
                min-height: auto;
            }
            
            .food-card-image {
                width: 100%;
                height: 200px;
            }
            
            .main-header h1 {
                font-size: 2.5rem;
            }
        }
            
        .tech-stack-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr); /* 4 kolom sejajar */
            gap: 20px;
            margin-top: 20px;
        }

        .tech-box {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            font-weight: 500;
            transition: transform 0.3s ease;
        }

        .tech-box:hover {
            transform: translateY(-5px);
        }

        .tech-box h4 {
            margin-bottom: 10px;
            font-size: 1.2rem;
        }

        @media (max-width: 1024px) {
            .tech-stack-grid {
                grid-template-columns: repeat(2, 1fr); /* 2 kolom jika layar mengecil */
            }
        }

        @media (max-width: 600px) {
            .tech-stack-grid {
                grid-template-columns: 1fr; /* 1 kolom di layar kecil */
            }
        }
            
        
    </style>
"""