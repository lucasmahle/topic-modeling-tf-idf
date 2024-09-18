from mahlemodel import MahleModel

model = MahleModel(words_per_topic=3)

model.fit_collection([
  'The recent surge in voter turnout has sparked discussions on the impact of grassroots mobilization in shaping election outcomes. As younger voters increasingly engage in political processes, experts suggest that this could signal a long-term shift in how policy priorities are set at both local and national levels. This newfound enthusiasm for civic participation may lead to changes in the way political campaigns are run, particularly as social media continues to be a powerful tool for political engagement.',
  'In an effort to tackle climate change and economic inequality, the government has introduced a series of policy reforms aimed at promoting green energy jobs while supporting low-income communities. These measures include subsidies for renewable energy companies, tax breaks for small businesses adopting sustainable practices, and increased funding for public transportation infrastructure. Critics, however, argue that the proposed reforms do not go far enough to address the root causes of environmental degradation and poverty.',
  'Political polarization has become a defining feature of contemporary governance, with major policy debates on healthcare and education being shaped by stark ideological divides. As political parties move further apart on key issues, bipartisan solutions become harder to achieve. This growing divide raises concerns about the future of democratic discourse and whether the country can overcome the challenges posed by extreme partisanship in order to address pressing social and economic issues.',
  'During the annual summit on global cooperation, world leaders gathered to discuss strategies for pandemic preparedness and economic recovery. The COVID-19 pandemic exposed significant gaps in international collaboration, prompting calls for stronger global health infrastructure and more resilient economic frameworks. Leaders agreed on the need for a coordinated response to future crises, though debates over vaccine distribution and financial aid continue to hinder full consensus.',
  'A recent ruling by the Supreme Court has reshaped the legal landscape surrounding immigration, as the court upheld a controversial policy that tightens restrictions on asylum seekers. The decision has drawn sharp criticism from human rights organizations, who argue that it undermines the country’s commitment to providing refuge for those fleeing persecution. Proponents of the ruling claim that it is necessary to maintain border security and uphold immigration laws.',
  'Youth-led political movements are becoming increasingly influential, driving significant changes in government transparency and anti-corruption efforts. From organizing mass protests to utilizing social media platforms to raise awareness, young activists are demanding greater accountability from their leaders. These movements have gained momentum in many countries, often leading to tangible political reforms, though they still face resistance from entrenched political institutions.',
  'Amid growing public unrest, the opposition party has called for a vote of no confidence in the current administration following allegations of corruption and misconduct. The call comes after a series of investigative reports revealed questionable financial dealings involving high-ranking government officials. As pressure mounts, the ruling party faces the prospect of early elections, which could drastically alter the political landscape depending on the outcome of the vote.',
  'After weeks of negotiations, a coalition government was finally formed, uniting parties from across the political spectrum. The coalition’s platform focuses on progressive social policies, including expanding access to healthcare, addressing income inequality, and implementing comprehensive climate legislation. While some members of the coalition remain skeptical of long-term unity, the agreement reflects a broader desire for political stability in a time of widespread uncertainty.',
  'International relations between key global powers are at a critical juncture as trade agreements face renewed scrutiny. With protectionist policies gaining traction in several major economies, longstanding trade partnerships are being renegotiated. The rise of nationalism and economic self-interest has led to a reevaluation of globalization, with many governments prioritizing domestic industries over international cooperation, potentially leading to a reshaped global trade order.',
  'Widespread protests erupted across the country in response to high-profile cases of police misconduct, with demonstrators demanding comprehensive reforms in law enforcement and justice systems. The protests, driven by grassroots organizations and community leaders, have led to increased pressure on policymakers to pass legislation addressing police accountability, racial discrimination, and systemic injustice. While some reforms have been introduced, activists continue to push for more significant structural changes.'
])

model.calculate_topics(5)

topics = model.get_topics()
[print('Topic: ', topic) for topic in topics]

(first_document_topic_index, first_document_topic_relevance) = model.get_document_topics(0)[0]
print('First document topic: ', topics[first_document_topic_index], 'with relevance: ', first_document_topic_relevance)