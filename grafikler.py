import matplotlib.pyplot as plt

# ==========================================
# 1. BMS-WEBVIEW-1 VERİLERİ (Seyrek)
# ==========================================
bms_sup = ['0.01 (%1)', '0.005 (%0.5)', '0.002 (%0.2)']
bms_pref_time = [105, 132, 186]
bms_spade_time = [54, 118, 412]
bms_gsp_time = [12185, 69778, 268831]

bms_pref_mem = [24.3, 40.8, 62.1]
bms_spade_mem = [416.7, 462.7, 369.6]
bms_gsp_mem = [149.5, 224.3, 355.3]

# BMS Grafikleri Çizimi
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
fig1.suptitle('BMS-WebView-1 Veri Seti: Algoritma Performans Karşılaştırması', fontsize=14)

ax1.plot(bms_sup, bms_pref_time, 'o-', color='blue', lw=2, label='PrefixSpan')
ax1.plot(bms_sup, bms_spade_time, 's-', color='red', lw=2, label='SPADE')
ax1.plot(bms_sup, bms_gsp_time, 'x--', color='purple', lw=2, label='GSP')
ax1.set(title='Çalışma Süresi (Log Ölçek)', xlabel='Minimum Support', ylabel='Süre (ms)')
ax1.set_yscale('log')
ax1.legend()
ax1.grid(True, ls="--", alpha=0.5)

ax2.plot(bms_sup, bms_pref_mem, 'o-', color='blue', lw=2, label='PrefixSpan')
ax2.plot(bms_sup, bms_spade_mem, 's-', color='red', lw=2, label='SPADE')
ax2.plot(bms_sup, bms_gsp_mem, 'x--', color='purple', lw=2, label='GSP')
ax2.set(title='Bellek Tüketimi', xlabel='Minimum Support', ylabel='Bellek (MB)')
ax2.legend()
ax2.grid(True, ls="--", alpha=0.5)

# ==========================================
# 2. LEVIATHAN VERİLERİ (Yoğun)
# ==========================================
lev_sup = ['0.05 (%5)', '0.02 (%2)', '0.01 (%1)']
lev_pref_time = [576, 2123, 6759]
lev_spade_time = [640, 1921, 7445]
lev_gsp_time = [26024, 291705, None] # %1'de çöktü

lev_pref_mem = [100.3, 120.4, 145.7]
lev_spade_mem = [429.8, 507.7, 375.8]
lev_gsp_mem = [104.2, 185.9, None]

# Leviathan Grafikleri Çizimi
fig2, (ax3, ax4) = plt.subplots(1, 2, figsize=(14, 5))
fig2.suptitle('Leviathan Veri Seti: Algoritma Performans Karşılaştırması', fontsize=14)

ax3.plot(lev_sup, lev_pref_time, 'o-', color='blue', lw=2, label='PrefixSpan')
ax3.plot(lev_sup, lev_spade_time, 's-', color='red', lw=2, label='SPADE')
ax3.plot(lev_sup, lev_gsp_time, 'x--', color='purple', lw=2, label='GSP (Timeout >30dk)')
ax3.set(title='Çalışma Süresi (Log Ölçek)', xlabel='Minimum Support', ylabel='Süre (ms)')
ax3.set_yscale('log')
ax3.legend()
ax3.grid(True, ls="--", alpha=0.5)

ax4.plot(lev_sup, lev_pref_mem, 'o-', color='blue', lw=2, label='PrefixSpan')
ax4.plot(lev_sup, lev_spade_mem, 's-', color='red', lw=2, label='SPADE')
ax4.plot(lev_sup, lev_gsp_mem, 'x--', color='purple', lw=2, label='GSP')
ax4.set(title='Bellek Tüketimi', xlabel='Minimum Support', ylabel='Bellek (MB)')
ax4.legend()
ax4.grid(True, ls="--", alpha=0.5)

# ==========================================
# 3. ÖLÇEKLENEBİLİRLİK (Scalability)
# ==========================================
data_sizes = ['%25', '%50', '%75', '%100']
bms_scale = [95, 104, 136, 186]
lev_scale = [461, 1123, 1648, 2123]

fig3, ax5 = plt.subplots(figsize=(8, 5))
ax5.plot(data_sizes, bms_scale, 'o-', color='orange', lw=2, label='BMS-WebView-1 (Seyrek)')
ax5.plot(data_sizes, lev_scale, 'D-', color='green', lw=2, label='Leviathan (Yoğun)')
ax5.set(title='Ölçeklenebilirlik Analizi (PrefixSpan)', xlabel='Veri Kümesi Boyutu (%)', ylabel='Çalışma Süresi (ms)')
ax5.legend()
ax5.grid(True, ls="--", alpha=0.7)

# Tüm pencereleri ekranda göster
plt.show()