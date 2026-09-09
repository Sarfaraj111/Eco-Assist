"""
EcoAssist Knowledge Base
Comprehensive text corpus covering SDG 13, 11, 12, and 3
covering pollution, climate, sustainability, and health.
"""

SDG_DOCUMENTS = [
    # ─────────────────────────────────────────────────────────────
    # SDG 13 – Climate Action
    # ─────────────────────────────────────────────────────────────
    {
        "id": "sdg13_001",
        "sdg": "SDG 13",
        "title": "Understanding Climate Change",
        "content": """
Climate change refers to long-term shifts in global temperatures and weather patterns.
While some changes are natural, since the mid-20th century human activities — primarily
burning fossil fuels — have been the main driver. Greenhouse gases like CO2, methane (CH4),
and nitrous oxide (N2O) trap heat in the Earth's atmosphere, causing the greenhouse effect.

Key facts:
- Global average temperature has risen ~1.2°C above pre-industrial levels as of 2023.
- The Paris Agreement (2015) aims to limit warming to 1.5°C above pre-industrial levels.
- Sea levels are rising at ~3.3 mm/year due to melting ice sheets and thermal expansion.
- Extreme weather events (floods, droughts, wildfires) are increasing in frequency and intensity.
- CO2 levels have exceeded 420 ppm — highest in 3 million years.

What individuals can do:
- Reduce personal carbon footprint by switching to renewable energy.
- Choose plant-based foods more often (livestock accounts for 14.5% of global emissions).
- Use public transport, cycle, or walk instead of driving.
- Support climate-conscious policies and elected officials.
- Plant trees and protect existing forests.
        """,
        "tags": ["climate", "greenhouse gases", "CO2", "Paris Agreement", "temperature rise"]
    },
    {
        "id": "sdg13_002",
        "sdg": "SDG 13",
        "title": "Carbon Emissions and Mitigation Strategies",
        "content": """
Carbon emissions are the primary driver of anthropogenic climate change. The major sectors
contributing to global CO2 emissions are:
1. Energy (electricity and heat production): ~34%
2. Transport: ~16%
3. Industry: ~24%
4. Agriculture, forestry, land use: ~22%
5. Buildings: ~6%

Mitigation strategies:
- **Renewable Energy Transition**: Solar, wind, hydro, and geothermal energy produce little
  to no operational emissions. The cost of solar panels has dropped 89% in the last decade.
- **Energy Efficiency**: Improving insulation, LED lighting, and efficient appliances can
  cut building emissions by up to 50%.
- **Carbon Capture and Storage (CCS)**: Technology that captures CO2 at the source and
  stores it underground.
- **Reforestation**: Forests absorb ~2.6 billion tonnes of CO2 per year.
- **Electrification of Transport**: EVs produce 50-70% less lifecycle emissions than
  petrol/diesel vehicles when charged with clean electricity.
- **Carbon Pricing**: Carbon taxes and cap-and-trade systems incentivize emissions reduction.
- **Green Hydrogen**: Produced via electrolysis using renewable energy; zero-emission fuel.

Net-zero by 2050 requires cutting global emissions by 45% from 2010 levels by 2030.
        """,
        "tags": ["carbon emissions", "renewable energy", "mitigation", "net-zero", "carbon capture"]
    },
    {
        "id": "sdg13_003",
        "sdg": "SDG 13",
        "title": "Climate Change Adaptation",
        "content": """
Adaptation involves adjusting to the current and future effects of climate change.
Even if emissions are drastically reduced today, some warming is already locked in.

Key adaptation strategies:
- **Flood Defences**: Building sea walls, levees, and managed coastal retreat programs.
- **Drought-Resistant Crops**: Agricultural adaptation to changing rainfall patterns.
- **Early Warning Systems**: Alerts for extreme weather events to save lives.
- **Urban Heat Island Mitigation**: Green roofs, urban forests, and cool pavements reduce
  city temperatures by 1-5°C.
- **Water Conservation**: Rainwater harvesting, desalination, and efficient irrigation.
- **Climate-Resilient Infrastructure**: Roads, bridges, and buildings designed for
  extreme weather.
- **Ecosystem-Based Adaptation**: Restoring wetlands, mangroves, and forests as natural
  buffers against floods and storm surges.

Climate finance: Developing nations need $300 billion/year by 2030 to adapt effectively.
The Green Climate Fund (GCF) helps mobilize resources for vulnerable countries.
        """,
        "tags": ["adaptation", "flood", "drought", "resilience", "green infrastructure"]
    },
    # ─────────────────────────────────────────────────────────────
    # SDG 11 – Sustainable Cities and Communities
    # ─────────────────────────────────────────────────────────────
    {
        "id": "sdg11_001",
        "sdg": "SDG 11",
        "title": "Air Pollution in Cities",
        "content": """
Air pollution is the contamination of indoor or outdoor environments by chemical, physical,
or biological agents that modify the natural characteristics of the atmosphere.

Major urban air pollutants:
- **PM2.5 & PM10** (Particulate Matter): Tiny particles from vehicles, industry, and fires.
  PM2.5 penetrates deep into lungs; linked to cardiovascular and respiratory disease.
- **NO2 (Nitrogen Dioxide)**: Emitted by vehicles and power plants. Causes lung inflammation.
- **O3 (Ground-level Ozone)**: Formed by photochemical reactions. Damages airways.
- **SO2 (Sulfur Dioxide)**: From burning fossil fuels. Causes acid rain and respiratory harm.
- **CO (Carbon Monoxide)**: From incomplete combustion. Reduces oxygen delivery in blood.
- **VOCs (Volatile Organic Compounds)**: From paints, solvents, and vehicles.

WHO Air Quality Guidelines (2021):
- PM2.5: Annual mean ≤5 µg/m³ (global average is 40+ µg/m³ in many cities)
- NO2: Annual mean ≤10 µg/m³
- O3: Peak season mean ≤60 µg/m³

Solutions for urban air quality:
- Low Emission Zones (LEZs) restricting high-polluting vehicles
- Expanding electric public transport
- Urban green spaces and trees (absorb pollutants)
- Strict industrial emission controls
- Transition from coal cooking/heating to clean fuels
        """,
        "tags": ["air pollution", "PM2.5", "urban", "WHO guidelines", "NO2"]
    },
    {
        "id": "sdg11_002",
        "sdg": "SDG 11",
        "title": "Sustainable Urban Transport",
        "content": """
Transport accounts for ~16% of global CO2 emissions, with road vehicles responsible for
the majority. Cities can dramatically reduce emissions through sustainable mobility.

Principles of sustainable urban transport:
1. **Avoid**: Reduce the need to travel (mixed-use zoning, work-from-home).
2. **Shift**: Move from private cars to public transport, cycling, and walking.
3. **Improve**: Make remaining motorized transport cleaner (EVs, biofuels).

Key initiatives:
- **Bus Rapid Transit (BRT)**: High-capacity, fast bus systems at lower cost than metro.
- **Congestion Pricing**: Charges for driving in city centres (London, Stockholm, Singapore).
- **Cycling Infrastructure**: Protected bike lanes increase cycling rates 5-fold.
- **Walkable Cities**: 15-minute city concept — all amenities within a 15-minute walk/cycle.
- **Electric Vehicles**: Zero tailpipe emissions; effectiveness depends on electricity grid.
- **Multimodal Integration**: Seamless connections between bus, rail, cycling, and walking.
- **Shared Mobility**: Car-sharing and ride-pooling reduce vehicle numbers on roads.

Benefits: Reduced emissions, lower noise pollution, improved air quality, better public health,
reduced congestion, and more equitable access to the city.
        """,
        "tags": ["transport", "electric vehicles", "cycling", "BRT", "congestion", "mobility"]
    },
    {
        "id": "sdg11_003",
        "sdg": "SDG 11",
        "title": "Waste Management in Urban Areas",
        "content": """
Global waste generation is expected to reach 3.4 billion tonnes per year by 2050.
Poor waste management pollutes land, water, and air, and contributes to climate change
(landfills produce methane, a potent greenhouse gas).

Waste hierarchy (most to least preferred):
1. **Prevention**: Design products to use less material and last longer.
2. **Reuse**: Repair and repurpose items before discarding.
3. **Recycling**: Process materials into new products.
4. **Recovery**: Recover energy from waste (waste-to-energy).
5. **Disposal**: Landfill as last resort.

Key strategies:
- **Zero Waste Cities**: San Francisco, Ljubljana achieve 80%+ diversion from landfill.
- **Extended Producer Responsibility (EPR)**: Manufacturers take back products at end of life.
- **Composting**: Organic waste into compost reduces landfill methane and improves soil.
- **Circular Economy**: Design products for disassembly and material recovery.
- **Informal Waste Sector**: Recognise and support waste pickers in developing countries.
- **Single-Use Plastic Bans**: EU banned top 10 single-use plastics found on beaches.

Electronic waste (e-waste) is the fastest-growing waste stream: 53.6 million tonnes/year,
with only 17% formally recycled. E-waste contains toxic heavy metals (lead, mercury, cadmium).
        """,
        "tags": ["waste", "recycling", "circular economy", "plastic", "e-waste", "landfill"]
    },
    {
        "id": "sdg11_004",
        "sdg": "SDG 11",
        "title": "Green Buildings and Sustainable Architecture",
        "content": """
Buildings account for ~40% of global energy consumption and ~33% of CO2 emissions.
Green building standards and practices can drastically reduce this impact.

Key certifications:
- **LEED** (Leadership in Energy and Environmental Design) – USA
- **BREEAM** (Building Research Establishment Environmental Assessment Method) – UK
- **EDGE** – IFC standard for emerging markets
- **Passive House (Passivhaus)** – Ultra-low energy standard

Features of green buildings:
- High-performance insulation and triple-glazed windows
- Solar panels and on-site renewable energy generation
- Green roofs and walls (insulation + biodiversity)
- Rainwater harvesting and greywater recycling
- LED lighting with occupancy sensors
- Building Management Systems (BMS) for energy optimization
- Natural ventilation and daylighting

Net-zero buildings produce as much energy as they consume annually.
Embodied carbon (from construction materials) accounts for 11% of global emissions —
low-carbon materials like cross-laminated timber (CLT) and recycled steel are alternatives.

Retrofitting existing buildings is often more cost-effective than new construction and
can reduce energy use by 50-80%.
        """,
        "tags": ["green buildings", "LEED", "energy efficiency", "net-zero", "retrofitting"]
    },
    # ─────────────────────────────────────────────────────────────
    # SDG 12 – Responsible Consumption and Production
    # ─────────────────────────────────────────────────────────────
    {
        "id": "sdg12_001",
        "sdg": "SDG 12",
        "title": "Plastic Pollution: Causes, Effects, and Solutions",
        "content": """
Plastic pollution is one of the most pressing environmental crises. Over 400 million tonnes
of plastic are produced annually, with only 9% ever recycled. The rest ends up in landfills,
incinerated, or polluting the environment.

Key facts:
- 8-10 million tonnes of plastic enter the oceans each year.
- There are estimated 5 trillion pieces of plastic in the world's oceans.
- Microplastics (< 5mm) have been found in human blood, lungs, placentas, and breast milk.
- A plastic bag can take 20 years to decompose; a plastic bottle up to 450 years.
- Plastic production is set to triple by 2060 if no action is taken.

Impacts:
- Marine life ingestion and entanglement (1 million seabirds, 100,000 marine mammals die/year)
- Microplastic contamination of food chains
- Release of toxic chemicals (BPA, phthalates) affecting endocrine systems
- Clogging of drains causing urban flooding

Solutions:
- **Reduce**: Choose products with minimal packaging; refuse single-use plastics.
- **Reuse**: Reusable bags, bottles, and containers.
- **Replace**: Biodegradable and compostable alternatives (with caution — check certifications).
- **Redesign**: Industry redesigning products for recyclability.
- **Regulation**: Bans on single-use plastics, EPR schemes, deposit-return systems.
- **Clean-up**: River and ocean cleanup initiatives (Ocean Cleanup Project).
- **UN Global Plastics Treaty**: Legally binding treaty being negotiated (2024-2025).
        """,
        "tags": ["plastic pollution", "microplastics", "ocean", "recycling", "single-use plastic"]
    },
    {
        "id": "sdg12_002",
        "sdg": "SDG 12",
        "title": "Sustainable Food Systems and Food Waste",
        "content": """
The global food system is responsible for ~34% of global greenhouse gas emissions.
About one-third of all food produced for human consumption is lost or wasted — around
1.3 billion tonnes per year — while 828 million people face hunger.

Food waste by stage:
- Farms: 13.8% of food is lost before leaving the farm (improper storage, handling)
- Retail: 13% lost in supermarkets (over-ordering, cosmetic standards)
- Consumer: 17% wasted at household level (over-buying, poor storage)

Impacts of food waste:
- 8-10% of global greenhouse gas emissions
- Waste of water, land, and energy used in production
- Methane from decomposing food in landfills

Sustainable food choices:
- **Eat less meat and dairy**: Beef produces 60kg CO2e per kg — 20× more than legumes.
- **Choose seasonal and local produce**: Reduces transport emissions.
- **Reduce food waste**: Meal planning, proper storage, using leftovers.
- **Support regenerative agriculture**: Builds soil health and sequesters carbon.
- **Plant-based diets**: If everyone ate plant-based, agricultural land use could fall 75%.

Food labelling: "Best before" vs "Use by" — best before is about quality, not safety.
Confusion between the two accounts for significant avoidable waste.
        """,
        "tags": ["food waste", "sustainable diet", "agriculture", "plant-based", "emissions"]
    },
    {
        "id": "sdg12_003",
        "sdg": "SDG 12",
        "title": "Fast Fashion and Textile Pollution",
        "content": """
The fashion industry is responsible for:
- 10% of global carbon emissions (more than aviation + maritime combined)
- 20% of global wastewater pollution from dyeing and treatment
- 35% of microplastic pollution in oceans (from synthetic fabric washing)
- 85% of textiles sent to landfill or incinerated each year

Fast fashion model: Rapidly changing trends with very cheap, low-quality clothing designed
to be worn a few times then discarded.

Key impacts:
- Cotton production uses 2,700 litres of water per T-shirt
- The Aral Sea was largely drained due to cotton irrigation
- Garment workers, mostly women in the Global South, often face unsafe conditions and low wages
- Polyester and nylon release microplastics with every wash

Sustainable fashion choices:
- **Buy less, buy better**: Invest in durable, quality clothing.
- **Second-hand shopping**: Thrifting, vintage, clothes swaps.
- **Rent and share**: Clothing rental platforms for special occasions.
- **Care for clothes**: Washing at lower temperatures, avoiding tumble drying.
- **Choose natural fibres**: Organic cotton, linen, hemp, TENCEL (lyocell).
- **Support ethical brands**: Look for Fair Trade, GOTS, B Corp certifications.
- **Wash with a Guppyfriend bag**: Catches microplastics from synthetic fabrics.
        """,
        "tags": ["fast fashion", "textile", "microplastics", "sustainable fashion", "water pollution"]
    },
    {
        "id": "sdg12_004",
        "sdg": "SDG 12",
        "title": "Circular Economy Principles",
        "content": """
The circular economy is a model of production and consumption that eliminates waste
and keeps materials in use as long as possible. It contrasts with the linear 'take-make-dispose'
model.

Three core principles (Ellen MacArthur Foundation):
1. **Eliminate waste and pollution**: Design out waste at the start.
2. **Circulate products and materials**: Keep products and materials in use at their highest value.
3. **Regenerate nature**: Return nutrients to soil, restore ecosystems.

Business models in the circular economy:
- **Product as a Service (PaaS)**: Lease a product instead of owning it (e.g., Michelin charges
  per tyre kilometre, not per tyre).
- **Remanufacturing**: Restoring used products to like-new condition (e.g., Caterpillar).
- **Industrial Symbiosis**: One industry's waste becomes another's raw material.
- **Sharing Platforms**: Airbnb, Uber, tool libraries maximize asset utilisation.
- **Biomimicry**: Design inspired by nature's closed-loop systems.

Economic opportunity: Circular economy could generate $4.5 trillion in economic benefits
by 2030 and create 6 million new jobs globally.

Digital technologies (IoT, blockchain, AI) enable better tracking of materials through
supply chains, supporting circular business models.
        """,
        "tags": ["circular economy", "waste", "remanufacturing", "sustainable business", "design"]
    },
    # ─────────────────────────────────────────────────────────────
    # SDG 3 – Good Health and Well-being
    # ─────────────────────────────────────────────────────────────
    {
        "id": "sdg3_001",
        "sdg": "SDG 3",
        "title": "Health Effects of Air Pollution",
        "content": """
Air pollution is the single greatest environmental health risk, causing approximately
7 million premature deaths per year globally (WHO, 2023). It is linked to:

Short-term effects:
- Eye, nose, and throat irritation
- Coughing, wheezing, and shortness of breath
- Aggravation of asthma and heart disease
- Headaches and dizziness

Long-term effects:
- Chronic obstructive pulmonary disease (COPD)
- Lung cancer (PM2.5 classified as Group 1 carcinogen by IARC)
- Cardiovascular disease: PM2.5 enters bloodstream, causing inflammation
- Stroke (accounting for 24% of deaths linked to air pollution)
- Adverse pregnancy outcomes: low birth weight, preterm birth
- Neurological impacts: dementia, cognitive decline, children's brain development

Vulnerable groups:
- Children (lungs still developing)
- Elderly (reduced immune function)
- People with pre-existing conditions
- Outdoor workers
- Residents near major roads or industrial zones

Indoor air pollution (from cooking fires, poor ventilation) kills 3.8 million/year.
Around 2.6 billion people still cook using open fires or simple stoves burning biomass.
Clean cooking solutions: LPG, biogas, improved cookstoves, electric induction cookers.
        """,
        "tags": ["health", "air pollution", "PM2.5", "respiratory", "cardiovascular", "WHO"]
    },
    {
        "id": "sdg3_002",
        "sdg": "SDG 3",
        "title": "Water Pollution and Human Health",
        "content": """
Water pollution occurs when harmful substances contaminate water bodies, degrading water
quality and making it toxic to humans and the environment.

Sources of water pollution:
- **Industrial discharge**: Heavy metals (lead, mercury, arsenic), chemicals, thermal pollution.
- **Agricultural runoff**: Fertilisers (nitrates, phosphates) causing eutrophication;
  pesticides contaminating groundwater.
- **Sewage and wastewater**: Pathogens, pharmaceuticals, microplastics.
- **Oil spills**: Crude oil coats marine wildlife and destroys ecosystems.
- **Plastic pollution**: Microplastics in drinking water.
- **Mining**: Acid mine drainage, heavy metal leaching.

Health impacts:
- 2 billion people lack access to safe drinking water.
- Contaminated water causes cholera, typhoid, dysentery, and hepatitis A.
- Lead poisoning causes irreversible brain damage in children.
- Nitrate contamination causes "blue baby syndrome" (methemoglobinemia).
- Arsenic in groundwater (Bangladesh, West Bengal) causes skin lesions, cancer.
- PFAS ("forever chemicals") linked to cancer, thyroid disease, immune system effects.

Solutions:
- Wastewater treatment before discharge
- Riparian buffer zones along waterways
- Sustainable agriculture practices (precision fertilisation)
- WASH programmes (Water, Sanitation, Hygiene)
- Nature-based solutions: constructed wetlands, biofilters
        """,
        "tags": ["water pollution", "health", "drinking water", "heavy metals", "WASH", "PFAS"]
    },
    {
        "id": "sdg3_003",
        "sdg": "SDG 3",
        "title": "Soil Pollution and Its Health Effects",
        "content": """
Soil pollution involves the presence of toxic chemicals in soil at concentrations harmful
to human health and ecosystems. It affects ~3 million sites globally.

Major contaminants:
- **Heavy metals**: Lead, cadmium, arsenic, mercury from mining, industry, old paint, batteries.
- **Pesticides and herbicides**: Persistent organic pollutants (POPs) accumulate in food chains.
- **Petroleum hydrocarbons**: From fuel spills at petrol stations, pipelines.
- **Industrial chemicals**: PCBs, dioxins, chlorinated solvents.
- **Nitrates and phosphates**: From agricultural overuse of fertilisers.

Pathways to human exposure:
- Eating contaminated vegetables grown in polluted soil
- Dust inhalation from contaminated areas
- Children eating soil (pica behaviour)
- Contaminated groundwater entering drinking supply

Health impacts:
- Lead: neurotoxic even at low doses; stunts children's cognitive development
- Cadmium: kidney damage, bone disease (itai-itai disease)
- Arsenic: skin lesions, bladder and lung cancer
- Pesticides: endocrine disruption, reproductive harm, certain cancers

Remediation techniques:
- **Bioremediation**: Microorganisms breaking down contaminants
- **Phytoremediation**: Plants absorbing heavy metals (sunflowers, alpine pennycress)
- **Soil washing**: Removing contaminants with water/chemical solvents
- **Containment**: Capping contaminated sites to prevent exposure
        """,
        "tags": ["soil pollution", "heavy metals", "pesticides", "remediation", "health"]
    },
    {
        "id": "sdg3_004",
        "sdg": "SDG 3",
        "title": "Noise Pollution and Mental Health",
        "content": """
Noise pollution, often overlooked, has significant health consequences, particularly in
urban environments. The WHO estimates that 1 in 5 Europeans are exposed to noise levels
at night that are harmful to health.

Sources of noise pollution:
- Road traffic (dominant source in cities)
- Airports and aircraft overflights
- Railways
- Industrial and construction noise
- Neighbourhood noise (music, entertainment venues)

Health effects:
- **Sleep disturbance**: Most critical impact; sleep < 7h linked to obesity, diabetes, heart disease
- **Cardiovascular disease**: Chronic traffic noise exposure linked to hypertension and heart attacks
- **Cognitive impairment in children**: School children near airports/motorways show poorer reading
  comprehension and memory
- **Tinnitus and hearing loss**: From occupational and recreational noise
- **Mental health**: Anxiety, depression, and annoyance from persistent noise
- **Endocrine disruption**: Noise triggers cortisol (stress hormone) release

Solutions:
- Noise barrier walls along motorways
- Low-noise road surfaces and tyre standards
- Quiet zones near schools, hospitals, and residential areas
- Night flight restrictions near airports
- Green buffers (trees and hedgerows reduce noise by 5-10 dB)
- Urban planning: separating incompatible land uses
        """,
        "tags": ["noise pollution", "mental health", "sleep", "cardiovascular", "urban"]
    },
    {
        "id": "sdg3_005",
        "sdg": "SDG 3",
        "title": "Light Pollution and Its Effects",
        "content": """
Light pollution is the excessive or misdirected artificial light at night (ALAN). It has
grown 2% per year globally since the 1990s and affects both human health and ecosystems.

Types:
- **Sky glow**: Brightening of the night sky over inhabited areas
- **Glare**: Excessive brightness causing visual discomfort
- **Light trespass**: Light falling where it is not needed or wanted
- **Clutter**: Confusing groupings of light sources

Health effects:
- Disruption of circadian rhythms (body clock) by suppressing melatonin production
- Increased risk of breast and prostate cancer (shift workers, high ALAN exposure)
- Sleep disorders, insomnia, obesity risk
- Depression and mood disorders

Ecological effects:
- Sea turtle hatchlings disoriented away from the sea
- Migratory birds crash into lit buildings (up to 1 billion birds/year in USA alone)
- Insects (moths, fireflies) disrupted — pollination impacts
- Coral reef spawning cycles disrupted
- Predator-prey relationships altered

Solutions:
- Use warm-toned (amber/red) LED lights at night
- Full-cutoff fixtures that direct light downward only
- Dimming and smart lighting systems
- Dark sky preserves and ordinances
- Switch off unnecessary lights after hours
        """,
        "tags": ["light pollution", "circadian rhythm", "melatonin", "ecosystems", "dark sky"]
    },
    # ─────────────────────────────────────────────────────────────
    # Cross-cutting themes
    # ─────────────────────────────────────────────────────────────
    {
        "id": "cross_001",
        "sdg": "SDG 11 / SDG 13",
        "title": "Urban Heat Islands and Green Infrastructure",
        "content": """
Urban Heat Islands (UHIs) are metropolitan areas significantly warmer than surrounding rural
areas due to human activities. City centres can be 1-7°C warmer than surrounding areas.

Causes of UHI:
- Dark surfaces (asphalt, rooftops) absorb and re-emit solar radiation as heat
- Lack of vegetation and water bodies (no evaporative cooling)
- Waste heat from vehicles, air conditioners, and industry
- Dense building canyons trapping heat and reducing wind flow

Impacts:
- Increased energy demand for cooling (feedback loop worsening climate change)
- Heat-related illness and mortality (especially elderly)
- Worsened air quality (higher O3 formation at high temperatures)
- Intensified urban rainfall events

Green infrastructure solutions:
- **Urban trees**: A single tree can cool up to 70m² through shade and transpiration.
  London has ~8 million trees; 40% canopy cover reduces temperatures by 2°C.
- **Green roofs**: Reduce surface temperatures by 30-40°C compared to conventional rooftops.
- **Green walls**: Vertical gardens cool buildings and reduce noise.
- **Urban parks and water features**: Open water and ponds provide evaporative cooling.
- **Cool/reflective pavements**: High-albedo surfaces reflect sunlight back.
- **Urban rewilding**: Restoring natural ecosystems within city boundaries.

Singapore's "City in a Garden" concept and Melbourne's Urban Forest Strategy are global
exemplars of green city planning.
        """,
        "tags": ["urban heat island", "green infrastructure", "urban trees", "cooling", "cities"]
    },
    {
        "id": "cross_002",
        "sdg": "SDG 12 / SDG 3",
        "title": "Chemical Pollution and Human Health",
        "content": """
The world produces over 350,000 registered chemical substances. Many are poorly tested
for health and environmental impacts. Chemical pollution is considered a 'planetary boundary'
that humanity has already crossed.

Major classes of concern:
- **Endocrine Disrupting Chemicals (EDCs)**: BPA, phthalates, parabens, pesticides.
  Interfere with hormonal signalling — linked to infertility, obesity, cancer.
- **PFAS (Per- and polyfluoroalkyl substances)**: 'Forever chemicals' used in non-stick
  cookware, food packaging, firefighting foam. Persist indefinitely in environment and
  human body. Linked to kidney cancer, thyroid disease, immune suppression.
- **Heavy metals**: Lead, mercury, cadmium, arsenic from industrial processes.
- **Persistent Organic Pollutants (POPs)**: DDT, PCBs, dioxins. Banned in many countries
  but still detected globally due to persistence.
- **Pesticides**: 4 million tonnes applied globally per year; contaminate food, water, and soil.

Regulatory frameworks:
- EU REACH (Registration, Evaluation, Authorisation, and Restriction of Chemicals)
- Stockholm Convention on POPs
- Minamata Convention on Mercury
- Rotterdam Convention on Prior Informed Consent

Safer alternatives:
- Green chemistry: Design chemicals and products to be safe and sustainable from the outset.
- Substitution: Replace hazardous chemicals with safer alternatives.
        """,
        "tags": ["chemicals", "PFAS", "EDC", "pesticides", "heavy metals", "health", "regulation"]
    },
    {
        "id": "cross_003",
        "sdg": "SDG 13 / SDG 3",
        "title": "Climate Change and Health Impacts",
        "content": """
Climate change is increasingly recognised as the greatest threat to global health in the
21st century (Lancet Countdown). It affects health through multiple pathways.

Direct impacts:
- **Extreme heat**: Heat stress and heat stroke; 356,000 heat-related deaths/year worldwide.
  By 2050, heat could make South Asian and Middle Eastern cities uninhabitable.
- **Extreme weather**: Injuries and deaths from floods, storms, and wildfires.
- **Air quality**: Higher temperatures worsen O3 and pollen levels.

Indirect impacts:
- **Food security**: Crop yield reductions from drought, floods, and pests.
- **Water security**: Glacial melt threatening freshwater supply for billions.
- **Infectious disease**: Mosquito-borne diseases (malaria, dengue, Zika) expanding range
  as temperatures rise. Tick-borne diseases increasing in Europe.
- **Mental health**: Climate anxiety, eco-grief, trauma from disasters.
- **Displacement**: Climate refugees — 1.2 billion people at risk by 2050.

Health co-benefits of climate action:
- Switching from fossil fuels to clean energy could prevent 3.6 million premature deaths/year.
- Active travel (cycling, walking) reduces emissions AND improves physical and mental health.
- Plant-based diets reduce emissions AND lower risk of heart disease, type 2 diabetes, cancer.

Climate-resilient health systems: WHO guidance calls for health systems to assess climate
vulnerability and integrate adaptation into health planning.
        """,
        "tags": ["climate health", "heat stress", "disease", "mental health", "co-benefits"]
    },
    {
        "id": "cross_004",
        "sdg": "SDG 11 / SDG 12",
        "title": "Marine and Ocean Pollution",
        "content": """
The ocean covers 71% of Earth's surface and provides ecosystem services worth $24 trillion/year.
It absorbs 30% of CO2 and 90% of excess heat from climate change. Yet it faces multiple
pollution threats.

Types of ocean pollution:
- **Plastic pollution**: 8-10 million tonnes/year; Great Pacific Garbage Patch is twice
  the size of Texas. Microplastics found in deepest ocean trenches.
- **Nutrient pollution (eutrophication)**: Agricultural runoff causes algal blooms that
  deplete oxygen, creating 'dead zones'. Over 500 dead zones globally.
- **Chemical pollution**: Pesticides, pharmaceuticals, heavy metals accumulate in marine food webs.
- **Oil pollution**: Shipping accidents, platform spills, and chronic discharge from ships.
- **Noise pollution**: Shipping and sonar disrupt whale and dolphin communication.
- **Thermal pollution**: Discharge from power plants raises local water temperatures.
- **Acidification**: Ocean absorbs CO2 → forms carbonic acid → pH falling (now 8.1, down from 8.2
  pre-industrial) → dissolves coral skeletons and shellfish shells.

Impact on health and food security:
- 3.3 billion people depend on seafood as primary protein source.
- Microplastics and chemical contaminants accumulate up food chains to human plates.
- Coral bleaching threatens fish populations relied on by 500 million people.

Solutions:
- Marine Protected Areas (MPAs): Currently 8% of oceans protected; target is 30% by 2030.
- Improving land-based waste management.
- Sustainable fishing and aquaculture practices.
- The High Seas Treaty (2023): First legal framework for protecting international waters.
        """,
        "tags": ["ocean", "marine pollution", "plastic", "acidification", "eutrophication", "coral"]
    },
    {
        "id": "action_001",
        "sdg": "SDG 13 / SDG 12",
        "title": "Individual and Community Climate Actions",
        "content": """
While systemic change is essential, individual actions — especially in high-income countries
— can meaningfully reduce emissions and inspire broader change.

High-impact individual actions (ranked by CO2 saved/year):
1. Have one fewer child: ~58 tonnes CO2e/year (lifetime impact)
2. Live car-free: ~2.4 tonnes CO2e/year
3. Avoid one transatlantic flight: ~1.6 tonnes CO2e/year (return)
4. Switch to plant-based diet: ~0.8 tonnes CO2e/year
5. Buy green energy: ~1.5 tonnes CO2e/year
6. Buy less stuff: variable but significant

Community actions:
- **Community energy projects**: Collectively owned renewable energy installations.
- **Repair cafés and tool libraries**: Reduce consumption through sharing.
- **Community gardens**: Local food production, biodiversity, community well-being.
- **Citizen science**: Participate in air quality monitoring, tree counting, wildlife surveys.
- **Climate advocacy**: Joining or supporting climate groups, contacting elected representatives.
- **Divestment**: Moving savings and pensions to fossil-fuel-free funds.

Business actions:
- Science-Based Targets (SBTi): Commit to emissions aligned with 1.5°C pathway.
- B Corp certification: High social and environmental standards.
- Sustainability reporting: GRI, TCFD, CSRD disclosure frameworks.

"Never doubt that a small group of thoughtful, committed citizens can change the world.
Indeed, it is the only thing that ever has." — Margaret Mead
        """,
        "tags": ["individual action", "carbon footprint", "community", "advocacy", "lifestyle"]
    },
]
