# 🎵 Spotify Portfolio Strategy & Streaming Growth Optimization

## 📌 Executive Summary
This project analyzes streaming patterns across 730 top Spotify tracks using the **PACE Framework** to optimize release strategies, feature bookings, and ad-spend allocation for an independent record label.

* **The Collaboration Dividend:** Multi-artist tracks generate **~28.4% higher average daily stream volume** than solo releases. However, efficiency peaks at **2 credited artists**; adding 3 or more yields diminishing returns.
* **Capitalizing on Momentum:** Using a custom **Viral Momentum Index**, we isolated catalog tracks outperforming their historical play counts in daily velocity, identifying prime candidates for ad-spend acceleration.
* **Market Concentration:** Platform traffic exhibits a strong Pareto distribution: the **top 10% of tracks command over 35% of daily streaming volume**.

---

## 🏢 Business Context
A mid-sized independent record label is preparing its multi-million dollar release strategy and promotional budget for upcoming tracks. Historically, label executives relied on intuition and traditional radio metrics to negotiate artist collaborations, schedule marketing push windows, and allocate budgets between solo projects and featured features. With streaming now driving the majority of industry revenue, the marketing team needs empirical data to maximize daily streaming performance and overall long-term reach on platforms like Spotify.

---

## 🎯 Core Problem Statement
How can the label optimize its artist signing, collaboration models, and release promotional strategies to maximize both immediate daily streaming velocity and sustained long-term track play counts?

---

## 🔍 Key Business & Research Questions

* **The Collaboration Premium:** Do collaborative tracks (`is_collaboration` = `True`) consistently achieve higher total streams (`spotify_streams_total`) or daily streaming velocity (`daily_streams`) compared to solo releases? Does increasing the number of credited artists (`billed_artist_count`) yield diminishing returns?
* **Daily Momentum vs. All-Time Giants:** What is the correlation between a track's total stream count (`spotify_streams_total`) and its current daily velocity (`daily_streams`)? Which tracks display high daily momentum despite having lower total historical plays, representing emerging viral hits worth immediate ad-spend backing?
* **Market Concentration:** What share of total platform consumption (`daily_stream_share_pct`) is captured by the top tier of tracks versus the tail?
* **Elite Visibility Impact:** What characteristics set apart the few tracks that break into top-tier global curated lists (`wrapped_global_top10_rank`) versus general top-performing catalog tracks?

---

## 📋 PACE Analytical Roadmap

1. **Plan:** Establish business rules for negotiating features, timing marketing spend, and maximizing promotional ROI.
2. **Analyze:** Inspect streaming distributions, evaluate top-performing artists, and test correlations between daily velocity and total streams.
3. **Construct:** Conduct non-parametric hypothesis testing (Mann-Whitney U) and feature engineer the **Viral Momentum Index** ($VMI$).
4. **Execute:** Translate statistical insights into clear, actionable commercial recommendations for label executives.

---

## 📦 Deliverables & Data Outputs

1. **Collaboration Performance Framework:** A statistical analysis comparing the mean/median daily streams and total streams of solo vs. multi-artist tracks to guide future feature bookings and contract negotiations.
2. **Viral Momentum Matrix:** A custom scoring metric combining `daily_streams_rank` and overall `rank` to identify underrated catalog tracks that are accelerating faster than expected.
3. **Portfolio Concentration Report:** A distribution curve evaluating `daily_stream_share_pct` to show how market share concentrates among top-ranked tracks.

---

## 📊 Key Findings & Visualizations

### 1. The Collaboration Premium & Optimal Artist Count
Collaborative tracks consistently outperform solo releases in daily streaming velocity ($p < 0.05$). However, performance peaks at **2 credited artists**.

![Solo vs Collaboration](images/collab_vs_solo_streams.png)
![Artist Count Returns](images/artist_count_diminishing_returns.png)

### 2. Market Share Concentration
Streaming volume is heavily concentrated at the top tier, reinforcing the strategic necessity of securing launch-week playlisting.

![Market Share Concentration](images/market_concentration.png)

---

## 💡 Strategic Recommendations

1. **Standardize 2-Artist Feature Contracts:** Make 2-artist co-releases the default structure for growth pushes. Avoid 3+ artist features due to diminishing reach returns and complex royalty splits.
2. **Automated Ad-Spend Triggers:** Reallocate marketing funds dynamically to tracks exhibiting a high positive `rank_delta` to convert transient viral momentum into sustained catalog plays.
3. **Focus Budget on Launch Momentum:** Allocate 60% of single-release budgets toward first-week playlist pitching to break into the high-earning top 10% platform tier.

---

## 📁 Repository Structure
```text
spotify-streaming-strategy/
├── data/
│   ├── raw/                  # Place original CSV here
│   └── processed/            # Cleaned data / computed features
├── notebooks/
│   └── 01_exploratory_analysis.ipynb
├── images/                   # Exported chart PNGs for the README
│   ├── collab_vs_solo_streams.png
│   ├── artist_count_diminishing_returns.png
│   └── market_concentration.png
├── README.md                 # Primary executive summary
└── requirements.txt          # Dependencies (pandas, seaborn, scipy)
