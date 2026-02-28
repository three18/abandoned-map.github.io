```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Карта Заброшек</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: #000;
            color: #fff;
            overflow: hidden;
        }
        
        #map {
            height: 100vh;
            width: 100%;
            position: absolute;
            top: 0;
            left: 0;
            z-index: 1;
        }
        
        .header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            background: rgba(0, 0, 0, 0.95);
            border-bottom: 1px solid #333;
            padding: 12px 20px;
        }
        
        .filter-panel {
            position: fixed;
            top: 70px;
            left: 20px;
            z-index: 1000;
            background: rgba(10, 10, 10, 0.98);
            border: 1px solid #333;
            border-radius: 12px;
            padding: 16px;
            min-width: 220px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
        }
        
        .filter-item {
            display: flex;
            align-items: center;
            padding: 10px 12px;
            margin: 4px 0;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
            background: rgba(30, 30, 30, 0.5);
        }
        
        .filter-item:hover {
            background: rgba(50, 50, 50, 0.8);
        }
        
        .filter-checkbox {
            width: 18px;
            height: 18px;
            margin-right: 12px;
            accent-color: #3b82f6;
            cursor: pointer;
        }
        
        .marker-icon {
            width: 42px;
            height: 42px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            box-shadow: 0 3px 15px rgba(0,0,0,0.6);
            border: 3px solid rgba(255,255,255,0.2);
        }
        
        .marker-factory { background: linear-gradient(135deg, #dc2626, #991b1b); }
        .marker-bunker { background: linear-gradient(135deg, #7c3aed, #5b21b6); }
        .marker-house { background: linear-gradient(135deg, #16a34a, #15803d); }
        .marker-structure { background: linear-gradient(135deg, #ea580c, #c2410c); }
        .marker-other { background: linear-gradient(135deg, #6b7280, #374151); }
        
        .btn {
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            border: none;
        }
        
        .btn-primary {
            background: linear-gradient(135deg, #3b82f6, #1d4ed8);
            color: white;
        }
        
        .btn-primary:hover {
            background: linear-gradient(135deg, #2563eb, #1e40af);
        }
        
        .btn-secondary {
            background: #374151;
            color: white;
        }
        
        .btn-secondary:hover {
            background: #4b5563;
        }
        
        .modal {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.9);
            z-index: 2000;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        
        .modal.active {
            display: flex;
        }
        
        .modal-content {
            background: #111;
            border: 1px solid #333;
            border-radius: 16px;
            padding: 30px;
            max-width: 500px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
        }
        
        .input {
            width: 100%;
            padding: 12px 16px;
            background: #1f2937;
            border: 1px solid #374151;
            border-radius: 8px;
            color: white;
            margin-top: 6px;
        }
        
        .input:focus {
            outline: none;
            border-color: #3b82f6;
        }
        
        .side-panel {
            position: fixed;
            top: 0;
            right: -450px;
            width: 450px;
            height: 100vh;
            background: rgba(10, 10, 10, 0.98);
            border-left: 1px solid #333;
            z-index: 1000;
            transition: right 0.3s ease;
            overflow-y: auto;
        }
        
        .side-panel.active {
            right: 0;
        }
        
        .card {
            background: rgba(30, 30, 30, 0.6);
            border: 1px solid #333;
            border-radius: 12px;
            padding: 16px;
            margin: 8px 0;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .card:hover {
            background: rgba(40, 40, 40, 0.8);
            border-color: #3b82f6;
        }
        
        .badge {
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 600;
        }
        
        .badge-pending { background: #fbbf24; color: #1f2937; }
        .badge-approved { background: #22c55e; color: white; }
        .badge-rejected { background: #ef4444; color: white; }
        
        .role-admin { background: linear-gradient(135deg, #ef4444, #b91c1c); }
        .role-moderator { background: linear-gradient(135deg, #8b5cf6, #6d28d9); }
        .role-stalker { background: linear-gradient(135deg, #22c55e, #15803d); }
        
        .toast {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: #111;
            border: 1px solid #333;
            border-left: 4px solid #3b82f6;
            padding: 16px 24px;
            border-radius: 12px;
            z-index: 3000;
            display: none;
            animation: slideIn 0.3s ease;
        }
        
        .toast.active {
            display: block;
        }
        
        @keyframes slideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        
        .leaflet-control-zoom {
            border: none !important;
            box-shadow: 0 4px 20px rgba(0,0,0,0.5) !important;
        }
        
        .leaflet-control-zoom a {
            background: #111 !important;
            color: white !important;
            border: 1px solid #333 !important;
        }
        
        .close-btn {
            position: absolute;
            top: 15px;
            right: 15px;
            background: none;
            border: none;
            color: #9ca3af;
            font-size: 24px;
            cursor: pointer;
        }
        
        .close-btn:hover {
            color: white;
        }
    </style>
</head>
<body>
    <!-- Map -->
    <div id="map"></div>

    <!-- Header -->
    <header class="header">
        <div class="flex items-center justify-between">
            <div class="flex items-center space-x-4">
                <div class="flex items-center space-x-3">
                    <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #3b82f6, #1d4ed8); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 20px;">
                        🗺️
                    </div>
                    <h1 style="font-size: 20px; font-weight: 700; background: linear-gradient(135deg, #60a5fa, #3b82f6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                        Карта Заброшек
                    </h1>
                </div>
                <nav class="hidden md:flex items-center space-x-2" style="margin-left: 30px;">
                    <button onclick="showPanel('map')" class="btn btn-secondary" id="navMap">Карта</button>
                    <button onclick="showPanel('profile')" class="btn btn-secondary" id="navProfile">Профиль</button>
                    <button onclick="showPanel('moderation')" class="btn btn-secondary hidden" id="navModeration">Модерация</button>
                    <button onclick="showPanel('admin')" class="btn btn-secondary hidden" id="navAdmin">Админка</button>
                </nav>
            </div>
            <div class="flex items-center space-x-3">
                <div id="authButtons">
                    <button onclick="showModal('loginModal')" class="btn btn-primary">Вход</button>
                    <button onclick="showModal('registerModal')" class="btn btn-secondary">Регистрация</button>
                </div>
                <div id="userMenu" class="hidden flex items-center space-x-3">
                    <div style="display: flex; align-items: center; gap: 10px; background: rgba(50,50,50,0.5); padding: 8px 16px; border-radius: 10px;">
                        <div style="width: 32px; height: 32px; background: linear-gradient(135deg, #3b82f6, #1d4ed8); border-radius: 8px; display: flex; align-items: center; justify-content: center;">
                            <i class="fas fa-user"></i>
                        </div>
                        <div>
                            <span id="userName" style="font-weight: 600; font-size: 14px;"></span>
                            <span id="userRole" class="badge role-stalker" style="font-size: 10px;"></span>
                        </div>
                    </div>
                    <button onclick="logout()" class="btn btn-secondary" style="background: rgba(239, 68, 68, 0.2); color: #ef4444;">
                        <i class="fas fa-sign-out-alt"></i>
                    </button>
                </div>
                <button onclick="showModal('addObjectModal')" class="btn btn-primary hidden" id="addObjectBtn">
                    <i class="fas fa-plus"></i> Добавить
                </button>
            </div>
        </div>
    </header>

    <!-- Filter Panel -->
    <div class="filter-panel">
        <div class="flex items-center justify-between" style="margin-bottom: 12px;">
            <h3 style="font-weight: 700; color: #60a5fa;">
                <i class="fas fa-filter" style="margin-right: 8px;"></i>Фильтры
            </h3>
            <button onclick="toggleFilterPanel()" style="background: none; border: none; color: #9ca3af; cursor: pointer;">
                <i class="fas fa-chevron-up" id="filterIcon"></i>
            </button>
        </div>
        <div id="filterContent">
            <label class="filter-item">
                <input type="checkbox" class="filter-checkbox" data-category="factory" checked>
                <span style="display: flex; align-items: center; gap: 10px;">
                    <span style="width: 32px; height: 32px; border-radius: 8px; background: linear-gradient(135deg, #dc2626, #991b1b); display: flex; align-items: center; justify-content: center;">🏭</span>
                    <span>Заводы</span>
                </span>
            </label>
            <label class="filter-item">
                <input type="checkbox" class="filter-checkbox" data-category="bunker" checked>
                <span style="display: flex; align-items: center; gap: 10px;">
                    <span style="width: 32px; height: 32px; border-radius: 8px; background: linear-gradient(135deg, #7c3aed, #5b21b6); display: flex; align-items: center; justify-content: center;">🛡️</span>
                    <span>Бомбоубежища</span>
                </span>
            </label>
            <label class="filter-item">
                <input type="checkbox" class="filter-checkbox" data-category="house" checked>
                <span style="display: flex; align-items: center; gap: 10px;">
                    <span style="width: 32px; height: 32px; border-radius: 8px; background: linear-gradient(135deg, #16a34a, #15803d); display: flex; align-items: center; justify-content: center;">🏠</span>
                    <span>Дома</span>
                </span>
            </label>
            <label class="filter-item">
                <input type="checkbox" class="filter-checkbox" data-category="structure" checked>
                <span style="display: flex; align-items: center; gap: 10px;">
                    <span style="width: 32px; height: 32px; border-radius: 8px; background: linear-gradient(135deg, #ea580c, #c2410c); display: flex; align-items: center; justify-content: center;">🏗️</span>
                    <span>Структуры</span>
                </span>
            </label>
            <label class="filter-item">
                <input type="checkbox" class="filter-checkbox" data-category="other" checked>
                <span style="display: flex; align-items: center; gap: 10px;">
                    <span style="width: 32px; height: 32px; border-radius: 8px; background: linear-gradient(135deg, #6b7280, #374151); display: flex; align-items: center; justify-content: center;">📍</span>
                    <span>Другие</span>
                </span>
            </label>
            <div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid #333;">
                <label class="filter-item">
                    <input type="checkbox" class="filter-checkbox" id="showPending" checked>
                    <span style="display: flex; align-items: center; gap: 10px;">
                        <span style="width: 32px; height: 32px; border-radius: 8px; background: linear-gradient(135deg, #fbbf24, #d97706); display: flex; align-items: center; justify-content: center;">⏳</span>
                        <span>Непроверенные</span>
                    </span>
                </label>
            </div>
            <div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid #333;">
                <button onclick="toggleMapType()" class="btn btn-secondary" style="width: 100%;">
                    <i class="fas fa-satellite" style="margin-right: 8px;"></i>
                    <span id="mapTypeText">Спутник</span>
                </button>
            </div>
        </div>
    </div>

    <!-- Side Panel -->
    <div class="side-panel" id="sidePanel">
        <button onclick="closePanel()" class="close-btn"><i class="fas fa-times"></i></button>
        <div id="panelContent" style="padding: 20px;"></div>
    </div>

    <!-- Login Modal -->
    <div class="modal" id="loginModal">
        <div class="modal-content">
            <button onclick="hideModal('loginModal')" class="close-btn"><i class="fas fa-times"></i></button>
            <div style="text-align: center; margin-bottom: 24px;">
                <div style="width: 60px; height: 60px; background: linear-gradient(135deg, #3b82f6, #1d4ed8); border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 28px; margin: 0 auto 16px;">
                    🔐
                </div>
                <h2 style="font-size: 24px; font-weight: 700; margin-bottom: 8px;">Вход</h2>
                <p style="color: #9ca3af; font-size: 14px;">Введите данные для доступа</p>
            </div>
            <form onsubmit="login(event)">
                <div style="margin-bottom: 16px;">
                    <label style="color: #9ca3af; font-size: 14px;">Никнейм</label>
                    <input type="text" id="loginNickname" class="input" required>
                </div>
                <div style="margin-bottom: 24px;">
                    <label style="color: #9ca3af; font-size: 14px;">Пароль</label>
                    <input type="password" id="loginPassword" class="input" required>
                </div>
                <button type="submit" class="btn btn-primary" style="width: 100%; padding: 14px;">Войти</button>
            </form>
            <p style="text-align: center; margin-top: 20px; color: #9ca3af; font-size: 14px;">
                Нет аккаунта? <button onclick="hideModal('loginModal'); showModal('registerModal')" style="color: #60a5fa; background: none; border: none; cursor: pointer;">Зарегистрироваться</button>
            </p>
        </div>
    </div>

    <!-- Register Modal -->
    <div class="modal" id="registerModal">
        <div class="modal-content">
            <button onclick="hideModal('registerModal')" class="close-btn"><i class="fas fa-times"></i></button>
            <div style="text-align: center; margin-bottom: 24px;">
                <div style="width: 60px; height: 60px; background: linear-gradient(135deg, #22c55e, #15803d); border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 28px; margin: 0 auto 16px;">
                    📝
                </div>
                <h2 style="font-size: 24px; font-weight: 700; margin-bottom: 8px;">Регистрация</h2>
                <p style="color: #9ca3af; font-size: 14px;">Создайте аккаунт сталкера</p>
            </div>
            <form onsubmit="register(event)">
                <div style="margin-bottom: 16px;">
                    <label style="color: #9ca3af; font-size: 14px;">Никнейм</label>
                    <input type="text" id="registerNickname" class="input" required minlength="3">
                </div>
                <div style="margin-bottom: 24px;">
                    <label style="color: #9ca3af; font-size: 14px;">Пароль</label>
                    <input type="password" id="registerPassword" class="input" required minlength="4">
                </div>
                <button type="submit" class="btn btn-primary" style="width: 100%; padding: 14px; background: linear-gradient(135deg, #22c55e, #15803d);">Зарегистрироваться</button>
            </form>
            <p style="text-align: center; margin-top: 20px; color: #9ca3af; font-size: 14px;">
                Есть аккаунт? <button onclick="hideModal('registerModal'); showModal('loginModal')" style="color: #60a5fa; background: none; border: none; cursor: pointer;">Войти</button>
            </p>
        </div>
    </div>

    <!-- Add Object Modal -->
    <div class="modal" id="addObjectModal">
        <div class="modal-content">
            <button onclick="hideModal('addObjectModal')" class="close-btn"><i class="fas fa-times"></i></button>
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 24px;">
                <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #22c55e, #15803d); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 24px;">
                    ➕
                </div>
                <div>
                    <h2 style="font-size: 22px; font-weight: 700;">Добавить объект</h2>
                    <p style="color: #9ca3af; font-size: 13px;">Заполните информацию</p>
                </div>
            </div>
            <form onsubmit="addObject(event)">
                <div style="margin-bottom: 16px;">
                    <label style="color: #9ca3af; font-size: 14px;">Название</label>
                    <input type="text" id="objectTitle" class="input" required placeholder="Например: Завод Красный Октябрь">
                </div>
                <div style="margin-bottom: 16px;">
                    <label style="color: #9ca3af; font-size: 14px;">Категория</label>
                    <select id="objectCategory" class="input">
                        <option value="factory">🏭 Завод</option>
                        <option value="bunker">🛡️ Бомбоубежище</option>
                        <option value="house">🏠 Дом</option>
                        <option value="structure">🏗️ Структура</option>
                        <option value="other">📍 Другое</option>
                    </select>
                </div>
                <div style="margin-bottom: 16px;">
                    <label style="color: #9ca3af; font-size: 14px;">Координаты</label>
                    <div style="display: flex; gap: 10px;">
                        <input type="number" id="objectLat" step="0.000001" placeholder="Широта" class="input" required>
                        <input type="number" id="objectLng" step="0.000001" placeholder="Долгота" class="input" required>
                    </div>
                    <button type="button" onclick="selectOnMap()" style="margin-top: 8px; color: #60a5fa; background: none; border: none; cursor: pointer; font-size: 14px;">
                        <i class="fas fa-crosshairs" style="margin-right: 6px;"></i>Выбрать на карте
                    </button>
                </div>
                <div style="margin-bottom: 16px;">
                    <label style="color: #9ca3af; font-size: 14px;">Описание</label>
                    <textarea id="objectDescription" rows="3" class="input" required placeholder="Опишите объект..."></textarea>
                </div>
                <div style="margin-bottom: 16px;">
                    <label style="color: #9ca3af; font-size: 14px;">Сложность</label>
                    <select id="objectDifficulty" class="input">
                        <option value="easy">🟢 Лёгкий</option>
                        <option value="medium" selected>🟠 Средний</option>
                        <option value="hard">🔴 Сложный</option>
                    </select>
                </div>
                <button type="submit" class="btn btn-primary" style="width: 100%; padding: 14px; background: linear-gradient(135deg, #22c55e, #15803d);">Добавить</button>
            </form>
        </div>
    </div>

    <!-- Object Detail Modal -->
    <div class="modal" id="objectDetailModal">
        <div class="modal-content">
            <button onclick="hideModal('objectDetailModal')" class="close-btn"><i class="fas fa-times"></i></button>
            <div id="objectDetailContent"></div>
        </div>
    </div>

    <!-- Toast -->
    <div class="toast" id="toast">
        <span id="toastMessage"></span>
    </div>

    <script>
        // Data
        const categories = {
            factory: { name: 'Завод', icon: '🏭', color: 'marker-factory' },
            bunker: { name: 'Бомбоубежище', icon: '🛡️', color: 'marker-bunker' },
            house: { name: 'Дом', icon: '🏠', color: 'marker-house' },
            structure: { name: 'Структура', icon: '🏗️', color: 'marker-structure' },
            other: { name: 'Другое', icon: '📍', color: 'marker-other' }
        };

        const difficultyLabels = {
            easy: { label: 'Лёгкий', color: '#22c55e' },
            medium: { label: 'Средний', color: '#f97316' },
            hard: { label: 'Сложный', color: '#ef4444' }
        };

        let currentUser = null;
        let map = null;
        let markers = [];
        let tempMarker = null;
        let isSatellite = true;
        let satelliteLayer = null;
        let streetLayer = null;

        let objects = [
            {
                id: 1,
                title: 'Завод "Красный Октябрь"',
                category: 'factory',
                lat: 55.751244,
                lng: 37.618423,
                description: 'Заброшенный заводской комплекс 1960-х годов. Сохранились основные цеха.',
                difficulty: 'medium',
                status: 'approved',
                authorId: 3,
                authorName: 'StalkerPro',
                photos: [],
                createdAt: '2024-01-15',
                reviews: []
            },
            {
                id: 2,
                title: 'Бункер Холодной войны',
                category: 'bunker',
                lat: 55.755826,
                lng: 37.617300,
                description: 'Подземное убежище советской эпохи. Требуется снаряжение.',
                difficulty: 'hard',
                status: 'approved',
                authorId: 5,
                authorName: 'BunkerHunter',
                photos: [],
                createdAt: '2024-01-20',
                reviews: []
            },
            {
                id: 3,
                title: 'Заброшенный особняк',
                category: 'house',
                lat: 55.748000,
                lng: 37.625000,
                description: 'Двухэтажный дом с интересной архитектурой.',
                difficulty: 'easy',
                status: 'approved',
                authorId: 3,
                authorName: 'StalkerPro',
                photos: [],
                createdAt: '2024-02-01',
                reviews: []
            },
            {
                id: 4,
                title: 'Недостроенная эстакада',
                category: 'structure',
                lat: 55.760000,
                lng: 37.610000,
                description: 'Металлическая конструкция высотой 30 метров.',
                difficulty: 'hard',
                status: 'pending',
                authorId: 6,
                authorName: 'NewStalker',
                photos: [],
                createdAt: '2024-02-10',
                reviews: []
            },
            {
                id: 5,
                title: 'Водонапорная башня',
                category: 'other',
                lat: 55.745000,
                lng: 37.630000,
                description: 'Кирпичная башня 1950-х годов.',
                difficulty: 'medium',
                status: 'approved',
                authorId: 5,
                authorName: 'BunkerHunter',
                photos: [],
                createdAt: '2024-02-05',
                reviews: []
            }
        ];

        let users = [
            { id: 1, nickname: 'admin', password: 'admin123', role: 'admin' },
            { id: 2, nickname: 'moderator', password: 'mod123', role: 'moderator' },
            { id: 3, nickname: 'StalkerPro', password: 'stalker123', role: 'stalker' },
            { id: 4, nickname: 'Explorer', password: 'exp123', role: 'stalker' },
            { id: 5, nickname: 'BunkerHunter', password: 'bunker123', role: 'stalker' },
            { id: 6, nickname: 'NewStalker', password: 'new123', role: 'stalker' }
        ];

        // Init
        document.addEventListener('DOMContentLoaded', () => {
            initMap();
            loadUser();
            updateUI();
            renderMarkers();
            setupFilters();
        });

        function initMap() {
            map = L.map('map', { zoomControl: false }).setView([55.751244, 37.618423], 13);
            
            L.control.zoom({ position: 'bottomright' }).addTo(map);
            
            satelliteLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
                attribution: '© Esri'
            }).addTo(map);
            
            streetLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© OpenStreetMap'
            });
            
            map.on('click', (e) => {
                if (!document.getElementById('addObjectModal').classList.contains('hidden') === false) {
                    if (document.getElementById('addObjectModal').style.display === 'flex') {
                        setTempMarker(e.latlng);
                    }
                }
            });
        }

        function toggleMapType() {
            if (isSatellite) {
                map.removeLayer(satelliteLayer);
                streetLayer.addTo(map);
                document.getElementById('mapTypeText').textContent = 'Схема';
            } else {
                map.removeLayer(streetLayer);
                satelliteLayer.addTo(map);
                document.getElementById('mapTypeText').textContent = 'Спутник';
            }
            isSatellite = !isSatellite;
        }

        function loadUser() {
            const saved = localStorage.getItem('currentUser');
            if (saved) currentUser = JSON.parse(saved);
        }

        function saveUser() {
            if (currentUser) localStorage.setItem('currentUser', JSON.stringify(currentUser));
            else localStorage.removeItem('currentUser');
        }

        function login(e) {
            e.preventDefault();
            const nick = document.getElementById('loginNickname').value.trim();
            const pass = document.getElementById('loginPassword').value;
            const user = users.find(u => u.nickname.toLowerCase() === nick.toLowerCase() && u.password === pass);
            if (user) {
                currentUser = { ...user };
                saveUser();
                updateUI();
                hideModal('loginModal');
                showToast(`Добро пожаловать, ${user.nickname}!`);
                renderMarkers();
            } else {
                showToast('Неверный логин или пароль', true);
            }
        }

        function register(e) {
            e.preventDefault();
            const nick = document.getElementById('registerNickname').value.trim();
            const pass = document.getElementById('registerPassword').value;
            if (users.find(u => u.nickname.toLowerCase() === nick.toLowerCase())) {
                showToast('Пользователь существует', true);
                return;
            }
            const newUser = { id: users.length + 1, nickname: nick, password: pass, role: 'stalker' };
            users.push(newUser);
            currentUser = { ...newUser };
            saveUser();
            updateUI();
            hideModal('registerModal');
            showToast('Регистрация успешна!');
        }

        function logout() {
            currentUser = null;
            saveUser();
            updateUI();
            renderMarkers();
            showToast('Вы вышли');
        }

        function updateUI() {
            const authBtns = document.getElementById('authButtons');
            const userMenu = document.getElementById('userMenu');
            const addBtn = document.getElementById('addObjectBtn');
            const navMod = document.getElementById('navModeration');
            const navAdmin = document.getElementById('navAdmin');
            
            if (currentUser) {
                authBtns.classList.add('hidden');
                userMenu.classList.remove('hidden');
                document.getElementById('userName').textContent = currentUser.nickname;
                const roleEl = document.getElementById('userRole');
                roleEl.textContent = getRoleLabel(currentUser.role);
                roleEl.className = `badge role-${currentUser.role}`;
                if (['stalker', 'moderator', 'admin'].includes(currentUser.role)) addBtn.classList.remove('hidden');
                if (['moderator', 'admin'].includes(currentUser.role)) navMod.classList.remove('hidden');
                if (currentUser.role === 'admin') navAdmin.classList.remove('hidden');
            } else {
                authBtns.classList.remove('hidden');
                userMenu.classList.add('hidden');
                addBtn.classList.add('hidden');
                navMod.classList.add('hidden');
                navAdmin.classList.add('hidden');
            }
        }

        function getRoleLabel(role) {
            return { guest: 'Гость', stalker: 'Сталкер', moderator: 'Модератор', admin: 'Админ' }[role] || role;
        }

        function renderMarkers() {
            markers.forEach(m => map.removeLayer(m));
            markers = [];
            const active = Array.from(document.querySelectorAll('.filter-checkbox:checked')).map(cb => cb.dataset.category);
            const showPending = document.getElementById('showPending').checked;
            
            objects.forEach(obj => {
                if (!active.includes(obj.category)) return;
                if (obj.status === 'pending' && !showPending) return;
                const canSee = currentUser && currentUser.role !== 'guest';
                const isAuthor = currentUser && obj.authorId === currentUser.id;
                if (obj.status === 'pending' && !canSee && !isAuthor) return;
                
                const marker = createMarker(obj);
                marker.addTo(map);
                markers.push(marker);
            });
        }

        function createMarker(obj) {
            const cat = categories[obj.category];
            if (!currentUser || currentUser.role === 'guest') {
                const icon = L.divIcon({ className: 'custom-marker', html: '<div style="width:16px;height:16px;background:#374151;border-radius:50%;border:2px solid #6b7280;"></div>', iconSize: [16, 16] });
                const m = L.marker([obj.lat, obj.lng], { icon });
                m.on('click', () => showToast('Зарегистрируйтесь для деталей', true));
                return m;
            }
            const icon = L.divIcon({
                className: 'custom-marker',
                html: `<div class="marker-icon ${cat.color}">${cat.icon}</div>`,
                iconSize: [42, 42]
            });
            const m = L.marker([obj.lat, obj.lng], { icon });
            const status = obj.status === 'pending' ? '⏳ На проверке' : obj.status === 'approved' ? '✅ Проверено' : '❌ Отклонено';
            const statusClass = obj.status === 'pending' ? 'badge-pending' : obj.status === 'approved' ? 'badge-approved' : 'badge-rejected';
            const diff = difficultyLabels[obj.difficulty];
            m.bindPopup(`
                <div style="min-width:260px;background:#111;color:#fff;border-radius:12px;overflow:hidden;">
                    <div style="padding:16px;">
                        <h3 style="font-weight:700;margin-bottom:8px;">${obj.title}</h3>
                        <span class="badge ${statusClass}" style="margin-bottom:12px;display:inline-block;">${status}</span>
                        <div style="display:flex;gap:8px;margin-bottom:12px;">
                            <span style="background:#374151;padding:4px 10px;border-radius:6px;font-size:13px;">${cat.icon} ${cat.name}</span>
                            <span style="color:${diff.color};padding:4px 10px;border-radius:6px;font-size:13px;">${diff.label}</span>
                        </div>
                        <p style="color:#9ca3af;font-size:13px;margin-bottom:12px;">${obj.description.substring(0,100)}...</p>
                        <p style="color:#6b7280;font-size:12px;">👤 ${obj.authorName}</p>
                        <button onclick="showObjectDetail(${obj.id})" style="width:100%;margin-top:12px;padding:10px;background:linear-gradient(135deg,#3b82f6,#1d4ed8);border:none;border-radius:8px;color:#fff;cursor:pointer;font-weight:600;">Подробнее</button>
                    </div>
                </div>
            `);
            return m;
        }

        function setupFilters() {
            document.querySelectorAll('.filter-checkbox').forEach(cb => cb.addEventListener('change', renderMarkers));
        }

        function toggleFilterPanel() {
            const content = document.getElementById('filterContent');
            const icon = document.getElementById('filterIcon');
            if (content.style.display === 'none') {
                content.style.display = 'block';
                icon.className = 'fas fa-chevron-up';
            } else {
                content.style.display = 'none';
                icon.className = 'fas fa-chevron-down';
            }
        }

        function showPanel(panel) {
            const sidePanel = document.getElementById('sidePanel');
            const content = document.getElementById('panelContent');
            sidePanel.classList.add('active');
            
            if (panel === 'profile' && currentUser) {
                const userObjs = objects.filter(o => o.authorId === currentUser.id);
                content.innerHTML = `
                    <div style="text-align:center;margin-bottom:24px;">
                        <div style="width:80px;height:80px;background:linear-gradient(135deg,#3b82f6,#1d4ed8);border-radius:20px;display:flex;align-items:center;justify-content:center;font-size:40px;margin:0 auto 16px;">
                            <i class="fas fa-user"></i>
                        </div>
                        <h2 style="font-size:22px;font-weight:700;">${currentUser.nickname}</h2>
                        <span class="badge role-${currentUser.role}" style="margin-top:8px;display:inline-block;">${getRoleLabel(currentUser.role)}</span>
                    </div>
                    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:24px;">
                        <div style="background:rgba(50,50,50,0.3);border:1px solid #333;border-radius:12px;padding:16px;text-align:center;">
                            <p style="font-size:28px;font-weight:700;color:#60a5fa;">${userObjs.length}</p>
                            <p style="color:#9ca3af;font-size:13px;">Мои объекты</p>
                        </div>
                        <div style="background:rgba(50,50,50,0.3);border:1px solid #333;border-radius:12px;padding:16px;text-align:center;">
                            <p style="font-size:28px;font-weight:700;color:#22c55e;">${userObjs.filter(o=>o.status==='approved').length}</p>
                            <p style="color:#9ca3af;font-size:13px;">Проверено</p>
                        </div>
                    </div>
                    <h3 style="font-weight:700;margin-bottom:12px;">Мои объекты</h3>
                    <div style="display:flex;flex-direction:column;gap:8px;">
                        ${userObjs.map(o => `
                            <div class="card" onclick="showObjectDetail(${o.id})">
                                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                                    <span style="font-weight:600;">${o.title}</span>
                                    <span class="badge badge-${o.status}">${o.status==='pending'?'⏳':o.status==='approved'?'✅':'❌'}</span>
                                </div>
                                <p style="color:#9ca3af;font-size:13px;">${categories[o.category].icon} ${categories[o.category].name}</p>
                            </div>
                        `).join('') || '<p style="color:#6b7280;text-align:center;padding:20px;">Нет объектов</p>'}
                    </div>
                `;
            } else if (panel === 'moderation' && currentUser && ['moderator','admin'].includes(currentUser.role)) {
                const pending = objects.filter(o => o.status === 'pending');
                content.innerHTML = `
                    <h2 style="font-size:22px;font-weight:700;margin-bottom:16px;">🔍 Модерация</h2>
                    <p style="color:#9ca3af;margin-bottom:16px;">На проверке: ${pending.length}</p>
                    <div style="display:flex;flex-direction:column;gap:8px;">
                        ${pending.map(o => `
                            <div class="card" style="border-left:3px solid #fbbf24;">
                                <h3 style="font-weight:600;margin-bottom:8px;">${o.title}</h3>
                                <p style="color:#9ca3af;font-size:13px;margin-bottom:8px;">${categories[o.category].icon} ${categories[o.category].name} • ${o.authorName}</p>
                                <p style="color:#d1d5db;font-size:13px;margin-bottom:12px;">${o.description.substring(0,80)}...</p>
                                <div style="display:flex;gap:8px;">
                                    <button onclick="moderateObject(${o.id},'approved')" class="btn btn-primary" style="flex:1;background:rgba(34,197,94,0.2);color:#22c55e;">✅ Принять</button>
                                    <button onclick="moderateObject(${o.id},'rejected')" class="btn btn-primary" style="flex:1;background:rgba(239,68,68,0.2);color:#ef4444;">❌ Отклонить</button>
                                </div>
                            </div>
                        `).join('') || '<p style="color:#6b7280;text-align:center;padding:20px;">Нет на проверке</p>'}
                    </div>
                `;
            } else if (panel === 'admin' && currentUser && currentUser.role === 'admin') {
                content.innerHTML = `
                    <h2 style="font-size:22px;font-weight:700;margin-bottom:16px;">⚙️ Админка</h2>
                    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:24px;">
                        <div style="background:rgba(50,50,50,0.3);border:1px solid #333;border-radius:12px;padding:16px;">
                            <p style="font-size:28px;font-weight:700;color:#60a5fa;">${objects.length}</p>
                            <p style="color:#9ca3af;font-size:13px;">Объектов</p>
                        </div>
                        <div style="background:rgba(50,50,50,0.3);border:1px solid #333;border-radius:12px;padding:16px;">
                            <p style="font-size:28px;font-weight:700;color:#fbbf24;">${objects.filter(o=>o.status==='pending').length}</p>
                            <p style="color:#9ca3af;font-size:13px;">На проверке</p>
                        </div>
                        <div style="background:rgba(50,50,50,0.3);border:1px solid #333;border-radius:12px;padding:16px;">
                            <p style="font-size:28px;font-weight:700;color:#22c55e;">${users.length}</p>
                            <p style="color:#9ca3af;font-size:13px;">Пользователей</p>
                        </div>
                        <div style="background:rgba(50,50,50,0.3);border:1px solid #333;border-radius:12px;padding:16px;">
                            <p style="font-size:28px;font-weight:700;color:#a855f7;">${objects.filter(o=>o.status==='approved').length}</p>
                            <p style="color:#9ca3af;font-size:13px;">Проверено</p>
                        </div>
                    </div>
                    <h3 style="font-weight:700;margin-bottom:12px;">Пользователи</h3>
                    <div style="display:flex;flex-direction:column;gap:8px;">
                        ${users.map(u => `
                            <div class="card" style="display:flex;justify-content:space-between;align-items:center;">
                                <div>
                                    <p style="font-weight:600;">${u.nickname}</p>
                                    <span class="badge role-${u.role}" style="font-size:10px;">${getRoleLabel(u.role)}</span>
                                </div>
                                <select onchange="changeUserRole(${u.id},this.value)" style="background:#1f2937;border:1px solid #374151;border-radius:6px;padding:6px 10px;color:#fff;">
                                    <option value="stalker" ${u.role==='stalker'?'selected':''}>Сталкер</option>
                                    <option value="moderator" ${u.role==='moderator'?'selected':''}>Модератор</option>
                                    <option value="admin" ${u.role==='admin'?'selected':''}>Админ</option>
                                </select>
                            </div>
                        `).join('')}
                    </div>
                `;
            } else if (!currentUser) {
                content.innerHTML = `
                    <div style="text-align:center;padding:40px 20px;">
                        <div style="width:60px;height:60px;background:rgba(50,50,50,0.5);border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:28px;margin:0 auto 16px;">
                            🔒
                        </div>
                        <h3 style="font-weight:700;margin-bottom:8px;">Требуется вход</h3>
                        <p style="color:#9ca3af;margin-bottom:20px;">Войдите для доступа</p>
                        <button onclick="showModal('loginModal')" class="btn btn-primary">Войти</button>
                    </div>
                `;
            } else {
                content.innerHTML = '<p style="color:#6b7280;text-align:center;padding:40px;">Доступ ограничен</p>';
            }
        }

        function closePanel() {
            document.getElementById('sidePanel').classList.remove('active');
        }

        function changeUserRole(id, role) {
            const u = users.find(x => x.id === id);
            if (u) { u.role = role; showToast(`Роль изменена: ${getRoleLabel(role)}`); showPanel('admin'); }
        }

        function selectOnMap() {
            hideModal('addObjectModal');
            showToast('Кликните на карту');
            window.selectingCoords = true;
        }

        function setTempMarker(latlng) {
            if (tempMarker) map.removeLayer(tempMarker);
            tempMarker = L.marker(latlng).addTo(map);
            document.getElementById('objectLat').value = latlng.lat.toFixed(6);
            document.getElementById('objectLng').value = latlng.lng.toFixed(6);
            if (window.selectingCoords) {
                window.selectingCoords = false;
                showModal('addObjectModal');
            }
        }

        function addObject(e) {
            e.preventDefault();
            const newObj = {
                id: objects.length + 1,
                title: document.getElementById('objectTitle').value,
                category: document.getElementById('objectCategory').value,
                lat: parseFloat(document.getElementById('objectLat').value),
                lng: parseFloat(document.getElementById('objectLng').value),
                description: document.getElementById('objectDescription').value,
                difficulty: document.getElementById('objectDifficulty').value,
                status: 'pending',
                authorId: currentUser.id,
                authorName: currentUser.nickname,
                photos: [],
                createdAt: new Date().toISOString().split('T')[0],
                reviews: []
            };
            objects.push(newObj);
            hideModal('addObjectModal');
            renderMarkers();
            showToast('Объект добавлен!');
            if (tempMarker) { map.removeLayer(tempMarker); tempMarker = null; }
            e.target.reset();
        }

        function showObjectDetail(id) {
            const obj = objects.find(o => o.id === id);
            if (!obj) return;
            const cat = categories[obj.category];
            const diff = difficultyLabels[obj.difficulty];
            const canMod = currentUser && ['moderator','admin'].includes(currentUser.role);
            const canEdit = currentUser && (obj.authorId === currentUser.id || canMod);
            
            let actions = '';
            if (canMod && obj.status === 'pending') {
                actions += `<div style="display:flex;gap:10px;margin-top:16px;">
                    <button onclick="moderateObject(${obj.id},'approved')" class="btn btn-primary" style="flex:1;background:rgba(34,197,94,0.2);color:#22c55e;">✅ Принять</button>
                    <button onclick="moderateObject(${obj.id},'rejected')" class="btn btn-primary" style="flex:1;background:rgba(239,68,68,0.2);color:#ef4444;">❌ Отклонить</button>
                </div>`;
            }
            if (canEdit) {
                actions += `<button onclick="editObject(${obj.id})" class="btn btn-secondary" style="width:100%;margin-top:10px;">✏️ Редактировать</button>`;
            }
            if (currentUser && obj.status === 'approved') {
                actions += `<button onclick="addReview(${obj.id})" class="btn btn-primary" style="width:100%;margin-top:10px;">💬 Отзыв</button>`;
            }
            
            const statusClass = obj.status === 'pending' ? 'badge-pending' : obj.status === 'approved' ? 'badge-approved' : 'badge-rejected';
            const statusText = obj.status === 'pending' ? '⏳ На проверке' : obj.status === 'approved' ? '✅ Проверено' : '❌ Отклонено';
            
            document.getElementById('objectDetailContent').innerHTML = `
                <div style="margin-bottom:16px;">
                    <span class="badge ${statusClass}" style="margin-bottom:12px;display:inline-block;">${statusText}</span>
                    <span style="background:#374151;padding:6px 12px;border-radius:8px;font-size:14px;margin-left:8px;">${cat.icon} ${cat.name}</span>
                </div>
                <h2 style="font-size:24px;font-weight:700;margin-bottom:16px;">${obj.title}</h2>
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:20px;">
                    <div style="background:rgba(50,50,50,0.3);border:1px solid #333;border-radius:10px;padding:12px;">
                        <p style="color:#9ca3af;font-size:12px;">Сложность</p>
                        <p style="color:${diff.color};font-weight:600;">${diff.label}</p>
                    </div>
                    <div style="background:rgba(50,50,50,0.3);border:1px solid #333;border-radius:10px;padding:12px;">
                        <p style="color:#9ca3af;font-size:12px;">Координаты</p>
                        <p style="font-weight:600;font-size:13px;">${obj.lat.toFixed(6)}, ${obj.lng.toFixed(6)}</p>
                    </div>
                </div>
                <p style="color:#d1d5db;line-height:1.6;margin-bottom:20px;">${obj.description}</p>
                <p style="color:#6b7280;font-size:13px;margin-bottom:20px;">👤 ${obj.authorName} • 📅 ${obj.createdAt}</p>
                <div style="border-top:1px solid #333;padding-top:16px;">
                    <h3 style="font-weight:700;margin-bottom:12px;">Отзывы (${obj.reviews ? obj.reviews.length : 0})</h3>
                    ${obj.reviews && obj.reviews.length > 0 ? obj.reviews.map(r => `
                        <div style="background:rgba(50,50,50,0.3);border:1px solid #333;border-radius:10px;padding:12px;margin-bottom:8px;">
                            <p style="font-weight:600;font-size:14px;">${r.userName}</p>
                            <p style="color:#d1d5db;font-size:13px;margin-top:6px;">${r.content}</p>
                        </div>
                    `).join('') : '<p style="color:#6b7280;text-align:center;padding:16px;">Нет отзывов</p>'}
                </div>
                ${actions}
            `;
            showModal('objectDetailModal');
        }

        function moderateObject(id, status) {
            const obj = objects.find(o => o.id === id);
            if (obj) {
                obj.status = status;
                hideModal('objectDetailModal');
                renderMarkers();
                showToast(status === 'approved' ? 'Принято!' : 'Отклонено', status === 'rejected');
                showPanel('moderation');
            }
        }

        function editObject(id) {
            const obj = objects.find(o => o.id === id);
            if (!obj) return;
            document.getElementById('objectTitle').value = obj.title;
            document.getElementById('objectCategory').value = obj.category;
            document.getElementById('objectLat').value = obj.lat;
            document.getElementById('objectLng').value = obj.lng;
            document.getElementById('objectDescription').value = obj.description;
            document.getElementById('objectDifficulty').value = obj.difficulty;
            hideModal('objectDetailModal');
            showModal('addObjectModal');
            const btn = document.querySelector('#addObjectModal button[type="submit"]');
            btn.textContent = 'Сохранить';
            btn.onclick = (e) => {
                e.preventDefault();
                obj.title = document.getElementById('objectTitle').value;
                obj.category = document.getElementById('objectCategory').value;
                obj.lat = parseFloat(document.getElementById('objectLat').value);
                obj.lng = parseFloat(document.getElementById('objectLng').value);
                obj.description = document.getElementById('objectDescription').value;
                obj.difficulty = document.getElementById('objectDifficulty').value;
                hideModal('addObjectModal');
                renderMarkers();
                showToast('Сохранено!');
                btn.textContent = 'Добавить';
                btn.onclick = addObject;
            };
        }

        function addReview(id) {
            const content = prompt('Ваш отзыв:');
            if (content && currentUser) {
                const obj = objects.find(o => o.id === id);
                if (obj) {
                    if (!obj.reviews) obj.reviews = [];
                    obj.reviews.push({ id: Date.now(), userId: currentUser.id, userName: currentUser.nickname, content });
                    showToast('Отзыв добавлен!');
                    showObjectDetail(id);
                }
            }
        }

        function showModal(id) {
            document.getElementById(id).style.display = 'flex';
        }

        function hideModal(id) {
            document.getElementById(id).style.display = 'none';
        }

        function showToast(msg, isError = false) {
            const t = document.getElementById('toast');
            document.getElementById('toastMessage').textContent = msg;
            t.style.borderLeftColor = isError ? '#ef4444' : '#3b82f6';
            t.classList.add('active');
            setTimeout(() => t.classList.remove('active'), 3000);
        }

        document.addEventListener('keydown', e => {
            if (e.key === 'Escape') {
                document.querySelectorAll('.modal').forEach(m => m.style.display = 'none');
                closePanel();
            }
        });
    </script>
</body>
</html>
```
