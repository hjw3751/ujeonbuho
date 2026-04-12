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

# 2. 아미노산 이름 매핑 딕셔너리 (사용자 이해를 돕기 위함)
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

st.title("🧬 유전부호 해독 시각화 프로그램")
st.markdown("입력된 DNA 서열이 mRNA로 전사되고, 단백질로 번역되는 과정을 시각적으로 확인합니다.")

# 아미노산 약어표 (토글 형태로 숨겨서 깔끔하게 배치)
with st.expander("👉 **아미노산 약어 & 전체 이름 표 보기 (클릭)**"):
    col1, col2 = st.columns(2)
    items = list(AMINO_ACID_NAMES.items())
    half = len(items) // 2
    for abbr, full_name in items[:half]:
        col1.write(f"**{abbr}** : {full_name}")
    for abbr, full_name in items[half:]:
        col2.write(f"**{abbr}** : {full_name}")

st.markdown("---")

# 사용자로부터 DNA 서열 입력받기
dna_sequence = st.text_input("DNA 염기서열을 입력하세요 (A, T, G, C만 입력 가능)", "ATGCGTACGTTAGCTAGCTAA").upper()
dna_sequence = dna_sequence.replace(" ", "")

if dna_sequence:
    # [추가된 기능] 예외 처리: A, T, G, C가 아닌 문자가 있는지 검사
    valid_chars = set("ATGC")
    if not set(dna_sequence).issubset(valid_chars):
        st.error("🚨 오류: DNA 염기서열은 A, T, G, C만 포함해야 합니다. 오타가 없는지 확인해 주세요.")
    else:
        st.subheader("1. 전사 과정 (Transcription)")
        
        mrna_sequence = dna_sequence.replace('T', 'U')
        
        st.write("**입력된 DNA (주형 가닥):**")
        st.info(dna_sequence)
        st.write("**전사된 mRNA:** (T가 U로 치환됨)")
        st.success(mrna_sequence)
        st.markdown("---")

        st.subheader("2. 번역 과정 (Translation) 및 결과 시각화")
        
        start_index = mrna_sequence.find('AUG')
        
        if start_index == -1:
            st.warning("경고: 입력된 서열에서 개시 코돈(AUG)을 찾을 수 없습니다. 번역을 시작할 수 없습니다.")
        else:
            st.write(f"✓ **개시 코돈(AUG)**이 {start_index + 1}번째 위치에서 발견되었습니다. 해독틀(Reading Frame)을 설정합니다.")
            
            translated_codons = []
            translated_aas = []
            
            for i in range(start_index, len(mrna_sequence) - 2, 3):
                codon = mrna_sequence[i:i+3]
                amino_acid = CODON_TABLE.get(codon, "Unknown")
                
                translated_codons.append(codon)
                translated_aas.append(amino_acid)
                
                if amino_acid == 'Stop':
                    break
            
            st.write("▼ **코돈 및 아미노산 매핑 결과**")
            
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
                
            html_blocks += '</div>'
            st.markdown(html_blocks, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            final_protein = "".join([aa for aa in translated_aas if aa != 'Stop' and aa != 'Met(Start)'])
            final_protein = "M" + final_protein if final_protein else "M"
            
            st.write("**최종 합성된 아미노산 서열 (1문자 약어 표기):**")
            st.info(final_protein)
            
            # [추가된 기능] 단백질 탐색 안내 및 NCBI 3D 구조 링크
            st.markdown("---")
            st.subheader("🔍 이 서열은 어떤 단백질일까요?")
            st.markdown("""
            우리가 방금 번역한 짧은 서열만으로는 실제 존재하는 특정 단백질의 이름을 완벽히 알아내기 어렵습니다. 실제 단백질은 수백 개의 아미노산으로 이루어져 있기 때문입니다.
            하지만 전 세계의 과학자들은 **'BLAST'**라는 데이터베이스 검색 도구를 이용해 내가 찾은 짧은 서열이 어떤 단백질의 일부인지 알아냅니다.
            """)
            
            st.success("""
            **🧬 합성된 단백질의 실제 3D 구조와 정보를 탐구해보고 싶다면?** 아래 **NCBI (미국 국립생물공학정보센터)** 사이트로 이동하여 3D 구조 뷰어(Structure)나 BLAST를 이용해 보세요!
            
            👉 [NCBI 웹사이트 바로가기 (클릭)](https://www.ncbi.nlm.nih.gov/)
            """)
