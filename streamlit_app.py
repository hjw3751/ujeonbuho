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

# 웹 페이지 기본 설정
st.set_page_config(page_title="유전부호 해독기", page_icon="🧬", layout="wide")

st.title("🧬 유전부호 해독 시각화 프로그램")
st.markdown("입력된 DNA 서열이 mRNA로 전사(Transcription)되고, 단백질로 번역(Translation)되는 과정을 시각적으로 확인한다.")
st.markdown("---")

# 사용자로부터 DNA 서열 입력받기
dna_sequence = st.text_input("DNA 염기서열을 입력하세요 (예: ATGCGT...)", "ATGCGTACGTTAGCTAGCTAA").upper()
# 띄어쓰기 및 불필요한 공백 제거
dna_sequence = dna_sequence.replace(" ", "")

if dna_sequence:
    st.subheader("1. 전사 과정 (Transcription)")
    
    # [구현 포인트 1] 파이썬 문자열 치환 기능(replace)을 사용하여 T를 U로 변환
    mrna_sequence = dna_sequence.replace('T', 'U')
    
    st.write("**입력된 DNA (주형 가닥):**")
    st.info(dna_sequence)
    st.write("**전사된 mRNA:** (T가 U로 치환됨)")
    st.success(mrna_sequence)
    st.markdown("---")

    st.subheader("2. 번역 과정 (Translation) 및 결과 시각화")
    
    # [구현 포인트 2] 개시 코돈(AUG) 탐색
    start_index = mrna_sequence.find('AUG')
    
    if start_index == -1:
        st.warning("경고: 입력된 서열에서 개시 코돈(AUG)을 찾을 수 없습니다. 번역을 시작할 수 없습니다.")
    else:
        st.write(f"✓ **개시 코돈(AUG)**이 {start_index + 1}번째 위치에서 발견되었습니다. 해독틀(Reading Frame)을 설정합니다.")
        
        # 해독될 코돈과 아미노산을 담을 리스트
        translated_codons = []
        translated_aas = []
        
        # [구현 포인트 2] 3염기씩 슬라이싱하여 딕셔너리와 대조
        for i in range(start_index, len(mrna_sequence) - 2, 3):
            codon = mrna_sequence[i:i+3]
            amino_acid = CODON_TABLE.get(codon, "Unknown")
            
            translated_codons.append(codon)
            translated_aas.append(amino_acid)
            
            # 종결 코돈을 만나면 번역 중지
            if amino_acid == 'Stop':
                break
        
        # [구현 포인트 3] HTML/CSS를 활용한 블록 형태 UI 구성 및 특정 색상 하이라이팅
        st.write("▼ **코돈 및 아미노산 매핑 결과**")
        
        html_blocks = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px;">'
        
        for codon, aa in zip(translated_codons, translated_aas):
            # 색상 기본값 지정 (일반 코돈은 회색 바탕)
            codon_bg_color = "#f0f2f6"
            codon_text_color = "black"
            
            # 하이라이팅 조건: 개시 코돈은 붉은색(핑크), 종결 코돈은 푸른색 계열로 강조
            if codon == 'AUG':
                codon_bg_color = "#ffcccc" # 연한 붉은색
                codon_text_color = "#cc0000"
            elif aa == 'Stop':
                codon_bg_color = "#cce5ff" # 연한 푸른색
                codon_text_color = "#004085"

            # 하나의 코돈-아미노산 블록을 HTML로 생성
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
        
        # 생성된 HTML을 화면에 렌더링
        st.markdown(html_blocks, unsafe_allow_html=True)
        
        # 최종 단백질 서열(텍스트) 출력
        st.markdown("<br>", unsafe_allow_html=True)
        final_protein = "-".join([aa for aa in translated_aas if aa != 'Stop' and aa != 'Met(Start)'])
        final_protein = "Met-" + final_protein if final_protein else "Met"
        
        st.write("**최종 합성된 아미노산 서열 (단백질):**")
        st.info(final_protein)
