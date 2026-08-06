# 🎵 Spotify Portfolio Strategy & Streaming Growth Optimization

## 📌 Executive Summary
This project analyzes streaming metrics across 730 top Spotify tracks using the **PACE Framework** to establish data-driven release strategies, feature booking guidelines, and marketing spend allocations for an independent record label.

* **Solo Performance Dominance:** Solo releases account for **96.8% of top-charting tracks** (707 out of 730). Solo tracks generate over **$2.1\times$ higher mean daily streams** (~374.7k vs ~177.3k) than collaborative releases ($p = 0.98527$).
* **Strategic Ad-Spend Amplification:** Using a custom **Viral Momentum Index** ($\text{Rank Delta} = \text{Overall Rank} - \text{Daily Rank}$), we identified high-velocity catalog tracks (e.g., *Tus Mentiras* with a +525 rank boost) that warrant immediate marketing investment.
* **Top-Tier Concentration:** The **top 10% of tracks command 29.36% of all daily streaming volume**, making launch-week playlist placement critical to platform economics.

---

## 🏢 Business Context
A mid-sized independent record label is preparing its multi-million dollar release strategy and promotional budget. Historically, label executives relied on intuition and traditional radio metrics to negotiate artist features and schedule marketing windows. With streaming driving the majority of music industry revenue, the team requires empirical analysis to maximize daily streaming performance and catalog longevity on Spotify.

---

## 🎯 Core Problem Statement
How can the label optimize its artist signing, collaboration models, and release promotional strategies to maximize both immediate daily streaming velocity and sustained long-term track play counts?

---

## 🔍 Key Business & Research Questions

* **The Collaboration Premium:** Do collaborative tracks (`is_collaboration` = `True`) achieve higher total or daily streams compared to solo releases? Does increasing credited artists (`billed_artist_count`) yield diminishing returns?
* **Daily Momentum vs. All-Time Giants:** What is the correlation between a track's total stream count (`spotify_streams_total`) and its daily velocity (`daily_streams`)? Which lower-ranked catalog tracks exhibit strong daily momentum?
* **Market Concentration:** What percentage of total daily streaming volume (`daily_stream_share_pct`) is captured by the top tier of tracks versus the long tail?
* **Elite Visibility:** What metrics characterize tracks achieving placement on global curated lists (`wrapped_global_top10_rank`)?

---

## 📋 PACE Analytical Roadmap

1. **Plan:** Formulate empirical business guidelines for feature contract negotiations, ad-spend timing, and catalog reinvestment.
2. **Analyze:** Inspect data hygiene across 730 entries, evaluate stream distributions, and test cross-variable relationships.
3. **Construct:** Conduct non-parametric hypothesis testing (Mann-Whitney U) on solo vs. collab performance and compute the **Viral Momentum Index**.
4. **Execute:** Translate statistical findings into clear commercial recommendations for label management.

---

## 📦 Deliverables & Analytical Outputs

1. **Collaboration Performance Framework:** Non-parametric statistical proof comparing solo vs. collaborative streaming metrics to direct artist feature negotiations.
2. **Viral Momentum Matrix:** A ranking model identifying tracks accelerating faster in daily stream rank than their overall play count rank.
3. **Portfolio Concentration Report:** Market-share distribution tracking the concentration of daily platform traffic among top-ranked tracks.

---

## 📊 Key Findings & Data Insights

### 1. Solo vs. Collaboration Performance
Contrary to standard industry assumptions, solo releases severely outperform collaborative tracks across both daily velocity and cumulative volume in this dataset.

| Metric | Solo Tracks (`False`) | Collaboration Tracks (`True`) |
| :--- | :--- | :--- |
| **Track Count** | 707 (96.8%) | 23 (3.2%) |
| **Mean Daily Streams** | 374,705.80 | 177,274.74 |
| **Median Daily Streams** | 226,315.00 | 149,369.00 |
| **Mean Total Streams** | 235,980,500 | 163,619,800 |

* **Hypothesis Test:** Mann-Whitney U Test ($p = 0.98527$) confirms no statistically significant collaboration premium exists.

![Solo vs Collaboration](images/collab_vs_solo_streams.png)
![Artist Count Returns](images/artist_count_diminishing_returns.png)
![Alt Text](images/artist_count_diminishing_returns.png)
---

### 2. High-Momentum Catalog Targets
By calculating `rank_delta` (`rank` $-$ `daily_streams_rank`), we isolated sleeper tracks exhibiting high current velocity relative to historical streams:

| Overall Rank | Daily Rank | Rank Delta | Track Title | Artist | Daily Streams |
| :---: | :---: | :---: | :--- | :--- | :---: |
| 621 | 96 | **+525** | Tus Mentiras (En Vivo) | Moy Bobadilla | 661,275 |
| 619 | 126 | **+493** | Libu-Libong Buwan (Uuwian) | Kyle Raphael | 563,642 |
| 581 | 111 | **+470** | Sitaare (From "Ikkis") | Arijit Singh | 604,945 |
| 687 | 221 | **+466** | Ishqa Ve | Zeeshan Ali | 365,504 |
| 541 | 86 | **+455** | Lihat Kebunku (Taman Bunga) | Aku Jeje | 726,423 |

---

### 3. Streaming Concentration
* The **top 10% of tracks capture 29.36% of all daily streaming consumption**, demonstrating substantial platform concentration at the top.

![Market Share Concentration](images/market_concentration.png)

---

## 💡 Strategic Recommendations

1. **Capitalize on Solo Lead Singles:** Prioritize promotional funding and push windows for solo releases. Solo tracks demonstrate stronger average baseline velocity than feature co-releases in this tier.
2. **Restructure Collaboration Contracts:** Re-evaluate upfront feature payments and royalty split structures. Given that collaborative tracks underperform solo releases in daily volume, feature bookings should serve secondary cross-promotional goals rather than primary stream drivers.
3. **Automate Reinvestment via Rank Delta:** Reallocate unused promotional funds to catalog tracks displaying a positive `rank_delta` > +400 (e.g., *Tus Mentiras*). Amplifying tracks with existing viral momentum optimizes ad-spend conversion rates.

---

## 📁 Repository Structure

```text
spotify-streaming-strategy/
├── data/
│   ├── raw/                  # Original CSV dataset
│   └── processed/            # Feature-engineered outputs
├── notebooks/
│   └── 01_exploratory_analysis.ipynb
├── images/                   # Exported chart assets
│   ├── collab_vs_solo_streams.png
│   ├── artist_count_diminishing_returns.png
│   └── market_concentration.png
├── README.md                 # Primary project documentation
└── requirements.txt          # Python packages (pandas, seaborn, scipy)
