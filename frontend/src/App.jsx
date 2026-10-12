:root {
  font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  color: #edf7ff;
  background: #07131d;
  line-height: 1.5;
  font-weight: 400;
  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  min-width: 320px;
  min-height: 100vh;
  background: radial-gradient(circle at top, #0e2435 0%, #081822 35%, #050d13 100%);
  color: #edf7ff;
}

* {
  box-sizing: border-box;
}

a {
  color: inherit;
  text-decoration: none;
}

button, input, select {
  font: inherit;
}

.app-shell {
  width: min(1280px, calc(100vw - 32px));
  margin: 0 auto;
  padding: 20px 0 60px;
}

.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 0 24px;
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.brand-mark {
  width: 36px;
  height: 36px;
  border-radius: 12px;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, #4ecdc4, #67e8f9);
  color: #07131d;
  font-weight: 900;
}

.brand-name {
  font-weight: 800;
  letter-spacing: 0.02em;
}

.brand-sub {
  color: #9db8c8;
  font-size: 12px;
}

.nav {
  display: flex;
  gap: 18px;
  align-items: center;
  color: #c3d8e5;
}

.primary-button,
.secondary-button,
.action-button {
  border: none;
  border-radius: 14px;
  cursor: pointer;
  font-weight: 700;
  transition: transform 0.2s ease, opacity 0.2s ease;
}

.primary-button:hover,
.secondary-button:hover,
.action-button:hover {
  transform: translateY(-1px);
}

.primary-button {
  background: linear-gradient(135deg, #4ecdc4, #67e8f9);
  color: #07131d;
  padding: 12px 18px;
}

.secondary-button {
  background: rgba(255,255,255,0.04);
  color: #edf7ff;
  border: 1px solid rgba(255,255,255,0.09);
  padding: 12px 18px;
}

.action-button {
  background: rgba(17, 31, 42, 0.8);
  color: #edf7ff;
  border: 1px solid rgba(255,255,255,0.08);
  padding: 12px 16px;
}

.hero {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 28px;
  align-items: center;
  padding-top: 28px;
}

.eyebrow {
  display: inline-flex;
  padding: 8px 12px;
  border-radius: 999px;
  background: rgba(78,205,196,0.12);
  color: #4ecdc4;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.hero h1 {
  margin: 18px 0 16px;
  font-size: clamp(2.5rem, 5vw, 5rem);
  line-height: 0.96;
}

.hero p {
  max-width: 620px;
  color: #a8c5d7;
  font-size: 1.05rem;
  line-height: 1.7;
}

.hero-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 28px;
}

.globe-card,
.panel,
.metric-card,
.stat-card {
  background: rgba(16, 30, 40, 0.7);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 24px;
  box-shadow: 0 18px 60px rgba(0,0,0,0.25);
}

.globe-card {
  padding: 18px;
  min-height: 520px;
}

.globe-wrap {
  width: 100%;
  height: 460px;
  border-radius: 18px;
  overflow: hidden;
  background: linear-gradient(180deg, rgba(9,21,30,1), rgba(14,35,49,0.8));
}

.metrics {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 18px;
  margin-top: 28px;
}

.metric-card {
  padding: 18px 20px;
}

.metric-card .label {
  color: #9fb9c8;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.metric-card .value {
  margin-top: 10px;
  font-size: clamp(1.6rem, 2vw, 2.3rem);
  font-weight: 800;
}

.metric-card .delta {
  margin-top: 8px;
  color: #7ae582;
  font-weight: 700;
  font-size: 12px;
}

.main-grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 22px;
  margin-top: 30px;
}

.panel {
  padding: 22px;
}

.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 18px;
}

.panel-title {
  margin: 0;
  font-size: 1.1rem;
}

.sparkline {
  height: 210px;
  display: flex;
  align-items: end;
  gap: 12px;
  padding: 14px 8px 4px;
  border-radius: 18px;
  background: linear-gradient(180deg, rgba(10, 26, 36, 0.9), rgba(15, 28, 39, 0.7));
  position: relative;
  overflow: hidden;
}

.sparkline-bar {
  flex: 1;
  border-radius: 10px 10px 0 0;
  background: linear-gradient(180deg, #4ecdc4 0%, #18354d 100%);
}

.form-grid {
  display: grid;
  gap: 14px;
}

.field {
  display: grid;
  gap: 8px;
}

.field span {
  color: #a9c2d3;
  font-size: 13px;
}

.field input,
.field select {
  width: 100%;
  background: rgba(3, 15, 22, 0.85);
  border: 1px solid rgba(255,255,255,0.08);
  color: #edf7ff;
  border-radius: 12px;
  padding: 12px 14px;
}

.field input[type='file'] {
  padding: 10px;
}

.result-box {
  margin-top: 16px;
  background: rgba(5, 16, 24, 0.84);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 12px;
  padding: 14px;
  color: #9feef8;
  white-space: pre-wrap;
  font-size: 13px;
  overflow: auto;
}

.status-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 12px;
  color: #cfe4f0;
  font-size: 13px;
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(122, 229, 130, 0.1);
  color: #7ae582;
  padding: 8px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 700;
}

@media (max-width: 980px) {
  .hero,
  .main-grid {
    grid-template-columns: 1fr;
  }

  .metrics {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 640px) {
  .metrics {
    grid-template-columns: 1fr;
  }

  .topbar {
    flex-direction: column;
    align-items: flex-start;
    gap: 14px;
  }

  .nav {
    flex-wrap: wrap;
  }
}
