# Gráficos por tipo de dado

Fonte: raw/charts.csv.

| dado | gráfico | alternativas | quando NÃO usar |
|---|---|---|---|
| Trend Over Time | Line Chart | Area Chart, Smooth Area | Fewer than 4 data points (use stat card); more than 6 series (visual noise); no time dimension exists |
| Compare Categories | Bar Chart (Horizontal or Vertical) | Column Chart, Grouped Bar | Categories > 15 (use table or search); data has time dimension (use line); showing proportions (use waffle/stacked) |
| Part-to-Whole | Pie Chart or Donut | Stacked Bar, Waffle Chart | Categories > 5; slice differences < 5% (visually indistinguishable); user needs precise values; accessibility-first context |
| Correlation / Distribution | Scatter Plot or Bubble Chart | Heat Map, Matrix | Variables are categorical (use grouped bar); fewer than 20 points (patterns aren't meaningful); mobile-primary context |
| Heatmap / Intensity | Heat Map or Choropleth | Grid Heat Map, Bubble Heat | Fewer than 20 cells (use bar); user needs to read exact values; colorblind users without pattern fallback |
| Geographic Data | Choropleth Map or Bubble Map | Geographic Heat Map | Regions have very different sizes making visual comparison misleading (use bar); raw counts or totals on a choropleth (normalize… |
| Funnel / Flow | Funnel Chart or Sankey | Waterfall (for flows) | Stages aren't sequential; values don't decrease monotonically (use bar); fewer than 3 stages |
| Performance vs Target | Gauge Chart or Bullet Chart | Dial, Thermometer | No target or benchmark exists; comparing multiple KPIs at once (use bullet chart grid) |
| Time-Series Forecast | Line with Confidence Band | Ribbon Chart | No historical baseline; prediction confidence is too low to be useful; audience is not data-literate |
| Anomaly Detection | Line Chart with Highlights | Scatter with Alert | Anomalies are predefined categories (use bar with highlight); real-time context without a pause control |
| Hierarchical / Nested Data | Treemap | Sunburst, Nested Donut, Icicle | Hierarchy depth > 3 levels (too complex to read); user needs to compare sibling values precisely |
| Flow / Process Data | Sankey Diagram | Alluvial, Chord Diagram | Flow directions form loops (use network graph); fewer than 3 source-target pairs; mobile-primary context |
| Cumulative Changes | Waterfall Chart | Stacked Bar, Cascade | Changes are not additive; more than 12 bars (readability breaks); audience expects a simple total |
| Multi-Variable Comparison | Radar / Spider Chart | Parallel Coordinates, Grouped Bar | Axes > 8 (unreadable); values need precise comparison (use grouped bar); audience unfamiliar with radar charts |
| Stock / Trading OHLC | Candlestick Chart | OHLC Bar, Heikin-Ashi | Non-financial audience; no OHLC data available (use line chart); accessibility-first context |
| Relationship / Connection Data | Network Graph | Hierarchical Tree, Adjacency Matrix | Node count > 500 without clustering pre-applied; user needs precise connection counts; mobile context |
| Distribution / Statistical | Box Plot | Violin Plot, Beeswarm | Fewer than 20 data points per group (distribution is not meaningful); audience unfamiliar with statistical charts |
| Performance vs Target (Compact) | Bullet Chart | Gauge, Progress Bar | Single KPI with emphasis (use gauge); data has no defined target range; fewer than 3 KPIs |
| Proportional / Percentage | Waffle Chart | Pictogram, Stacked Bar 100% | More than 5 categories (use stacked bar); exact values matter over visual proportion; very tight space |
| Hierarchical Proportional | Sunburst Chart | Treemap, Icicle, Circle Packing | More than 3 hierarchy levels (outer rings become unreadable); precision matters over overview; mobile |
| Root Cause Analysis | Decomposition Tree | Decision Tree, Flow Chart | No clear parent-child causal relationship; audience expects a summary rather than exploration |
| 3D Spatial Data | 3D Scatter / Surface Plot | Volumetric Rendering, Point Cloud | 2D projection conveys the same insight; mobile context; accessibility-required environments; standard business dashboards |
| Real-Time Streaming | Streaming Area Chart | Ticker Tape, Moving Gauge | Update frequency < 1/min (use periodic-refresh line chart); flashing content without reduced-motion support |
| Sentiment / Emotion | Word Cloud with Sentiment | Sentiment Arc, Radar Chart | Precise values matter (word size is inherently imprecise); screen-reader context; corpus < 50 items |
| Process Mining | Process Map / Graph | Directed Acyclic Graph (DAG), Petri Net | No event log data available; audience expects a static flowchart (use diagram tool); node count > 100 without pre-filtering |
