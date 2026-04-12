import streamlit as st

# 1. 파이썬 딕셔너리를 활용한 RNA 코돈표
CODON_TABLE = {
    'AUA': 'Ile', 'AUC': 'Ile', 'AUU': 'Ile', 'AUG': 'Met(Start)',
    'ACA': 'Thr', 'ACC': 'Thr', 'ACG': 'Thr', 'ACU': 'Thr',
    'AAC': 'Asn', 'AAU': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'AGC': 'Ser', 'AGU': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
    'CUA': 'Leu', 'CUC': 'Leu', 'CUG': 'Leu', 'CUU': 'Leu',
    'CCA': 'Pro', 'CCC': 'Pro', 'CCG': 'Pro', 'CCU': 'Pro',
    'CAC': 'His', 'CAU': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'CGA': 'Arg', 'CGC': 'Arg', 'CGG': 'Arg', 'CGU': 'Arg',
    'GUA': 'Val', 'GUC': 'Val', 'GUG': 'Val', 'GUU': 'Val',
    'GCA': 'Ala', 'GCC': 'Ala', 'GCG': 'Ala', 'GCU': 'Ala',
    'GAC': 'Asp', 'GAU': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
    'GGA': 'Gly', 'GGC': 'Gly', 'GGG': 'Gly', 'GGU': 'Gly',
    'UCA': 'Ser', 'UCC': 'Ser', 'UCG': 'Ser', 'UCU': 'Ser',
    'UUC': 'Phe', 'UUU': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'UAC': 'Tyr', 'UAU': 'Tyr', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGC': 'Cys', 'UGU': 'Cys', 'UGA': 'Stop', 'UGG': 'Trp',
}

AMINO_ACID_NAMES = {
    'Ile': '이소류신 (Isoleucine)', 'Met(Start)': '메싸이오닌 (Methionine) / 개시',
    'Thr': '트레오닌 (Threonine)', 'Asn': '아스파라긴 (Asparagine)',
    'Lys': '라이신 (Lysine)', 'Ser': '세린 (Serine)',
    'Arg': '아르기닌 (Arginine)', 'Leu': '류신 (Leucine)',
    'Pro': '프롤린 (Proline)', 'His': '히스티딘 (Histidine)',
    'Gln': '글루타민 (Glutamine)', 'Val': '발린 (Valine)',
    'Ala': '알라닌 (Alanine)', 'Asp': '아스파르트산 (Aspartic Acid)',
    'Glu': '글루탐산 (Glutamic Acid)', 'Gly': '글라이신 (Glycine)',
    'Phe': '페닐알라닌 (Phenylalanine)', 'Tyr': '타이로신 (Tyrosine)',
    'Cys': '시스테인 (Cysteine)', 'Trp': '트립토판 (Tryptophan)',
    'Stop': '종결 코돈 (Translation Stop)'
}

# 웹 페이지 기본 설정
st.set_page_config(page_title="유전부호 해독기", page_icon="🧬", layout="wide")

st.title("🧬 유전부호 해독 및 시각화 프로그램")
st.markdown("DNA 서열이 mRNA로 전사(Transcription)되고, 단백질로 번역(Translation)되는 과정을 시각적으로 확인한다.")
st.markdown("---")

# [추가된 기능 1] 생명과학 이론 설명 토글 (VectorBuilder 이미지 활용)
st.header("📚 생명현상 해석 가이드")

with st.expander("📖 1. 단백질 생성 과정 (Central Dogma)"):
    st.markdown("DNA의 유전 정보는 중간 산물인 mRNA로 전사된 후, 리보솜에서 단백질로 번역된다.")
    try:
        st.image("fig1_central_dogma.png", caption="Figure 1. DNA is transcribed and translated into functional proteins.")
    except:
        st.warning("안내: 'fig1_central_dogma.png' 파일을 코드와 같은 폴더에 넣으면 이미지가 표시됩니다.")

with st.expander("📖 2. 코돈표 (Codon Table)"):
    st.markdown("mRNA의 3개 염기(코돈)는 하나의 아미노산을 지정한다. 총 64개의 코돈이 20종류의 아미노산과 개시/종결을 지시한다.")
    try:
        st.image("fig2_codon_table.png", caption="Figure 2. Each three-letter nucleotide sequence corresponds to an amino acid.")
    except:
        st.warning("안내: 'fig2_codon_table.png' 파일을 코드와 같은 폴더에 넣으면 이미지가 표시됩니다.")

with st.expander("📖 3. 단백질의 구조 (Protein Structure)"):
    st.markdown("번역된 아미노산 사슬(1차 구조)은 꺾이고 접히며 입체 구조를 형성하고(2차, 3차), 여러 소단위체가 모여 복합체(4차 구조)를 이룬다.")
    try:
        st.image("fig3_protein_structure.png", caption="Figure 3. Structural organization of proteins.")
    except:
        st.warning("안내: 'fig3_protein_structure.png' 파일을 코드와 같은 폴더에 넣으면 이미지가 표시됩니다.")

with st.expander("📖 4. 틀 이동 돌연변이 (Frameshift Mutation)"):
    st.markdown("염기가 하나 삽입되거나 결실되면 코돈을 읽는 틀(Reading frame)이 밀려, 그 이후의 모든 아미노산 서열이 변하게 된다.")
    try:
        st.image("fig4_frameshift.png", caption="Figure 4. Consequences of a frameshift mutation.")
    except:
        st.warning("안내: 'fig4_frameshift.png' 파일을 코드와 같은 폴더에 넣으면 이미지가 표시됩니다.")

with st.expander("👉 아미노산 약어 & 전체 이름 표 보기"):
    col1, col2 = st.columns(2)
    items = list(AMINO_ACID_NAMES.items())
    half = len(items) // 2
    for abbr, full_name in items[:half]:
        col1.write(f"**{abbr}** : {full_name}")
    for abbr, full_name in items[half:]:
        col2.write(f"**{abbr}** : {full_name}")

st.markdown("---")

# 사용자로부터 DNA 서열 입력받기 (긴 서열을 위해 text_area 사용)
st.subheader("💻 번역기 실행")
dna_sequence = st.text_area("DNA 염기서열을 입력하세요 (길이가 길어도 무방함, A, T, G, C)", "ATGCGTACGTTAGCTAGCTAAGCTAGCTAGCATGCATCGA").upper()
dna_sequence = dna_sequence.replace(" ", "").replace("\n", "")

if dna_sequence:
    valid_chars = set("ATGC")
    if not set(dna_sequence).issubset(valid_chars):
        st.error("🚨 오류: DNA 염기서열은 A, T, G, C만 포함해야 합니다. 오타가 없는지 확인해 주세요.")
    else:
        st.markdown("#### 1. 전사 과정 (Transcription)")
        mrna_sequence = dna_sequence.replace('T', 'U')
        
        st.write("**입력된 DNA:**")
        st.info(dna_sequence)
        st.write("**전사된 mRNA:**")
        st.success(mrna_sequence)
        st.markdown("---")

        st.markdown("#### 2. 번역 과정 (Translation)")
        start_index = mrna_sequence.find('AUG')
        
        if start_index == -1:
            st.warning("경고: 입력된 서열에서 개시 코돈(AUG)을 찾을 수 없습니다.")
        else:
            st.write(f"✓ **개시 코돈(AUG)**이 발견되어 해독을 시작합니다.")
            
            translated_codons = []
            translated_aas = []
            
            for i in range(start_index, len(mrna_sequence) - 2, 3):
                codon = mrna_sequence[i:i+3]
                amino_acid = CODON_TABLE.get(codon, "Unknown")
                
                translated_codons.append(codon)
                translated_aas.append(amino_acid)
                
                if amino_acid == 'Stop':
                    break
            
            st.write("▼ **코돈-아미노산 매핑 시각화**")
            html_blocks = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px;">'
            
            for codon, aa in zip(translated_codons, translated_aas):
                codon_bg_color = "#f0f2f6"
                codon_text_color = "black"
                
                if codon == 'AUG':
                    codon_bg_color = "#ffcccc" 
                    codon_text_color = "#cc0000"
                elif aa == 'Stop':
                    codon_bg_color = "#cce5ff" 
                    codon_text_color = "#004085"

                block = f"""
                <div style="display: flex; flex-direction: column; align-items: center; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; width: 70px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">
                    <div style="background-color: {codon_bg_color}; color: {codon_text_color}; font-weight: bold; padding: 5px; width: 100%; text-align: center; border-bottom: 1px solid #ddd;">
                        {codon}
                    </div>
                    <div style="background-color: white; color: black; padding: 5px; width: 100%; text-align: center; font-size: 14px;">
                        {aa}
                    </div>
                </div>
                """
                html_blocks += block
                
            html_blocks += '</div><br>'
            st.markdown(html_blocks, unsafe_allow_html=True)
            
            # [추가된 기능 2] 긴 아미노산 서열을 10개 단위로 잘라서(Chunking) 출력
            raw_aa_list = [aa for aa in translated_aas if aa not in ('Stop', 'Met(Start)')]
            raw_aa_list.insert(0, 'M') # 개시 코돈 표기
            
            chunk_size = 10
            formatted_protein_chunks = []
            
            for i in range(0, len(raw_aa_list), chunk_size):
                chunk = "-".join(raw_aa_list[i:i+chunk_size])
                formatted_protein_chunks.append(chunk)
                
            final_display_text = "\n".join(formatted_protein_chunks)
            
            st.write("**최종 합성된 단백질 서열 (10개 단위 줄바꿈):**")
            st.code(final_display_text, language='text')
            
            st.markdown("---")
            st.subheader("🔍 이 서열의 실제 단백질 구조가 궁금하다면?")
            st.markdown("""
            실제 생명체의 단백질은 위와 같은 아미노산이 수백 개 연결되어 고유한 3차원 입체 구조를 형성합니다.
            전 세계 생물학자들은 NCBI 데이터베이스를 활용해 내가 찾은 서열의 기능을 분석합니다.
            """)
            st.success("""
            👉 [NCBI 웹사이트 바로가기](https://www.ncbi.nlm.nih.gov/)
            - **Structure 메뉴:** 이미 밝혀진 단백질의 3D 입체 구조를 돌려보며 관찰할 수 있습니다.
            - **BLAST 도구:** 위에서 번역한 서열을 입력하여 어떤 생명체의 단백질과 일치하는지 검색해 보세요!
            """)
