import streamlit as st

st.title("實驗六：真空抽氣性能實驗")
# 在這裡添加實驗一的具體內容，如圖表、數據等
st.markdown("### 國立虎尾科技大學機械設計工程系")
st.markdown("### 113學年度『機械工程實驗(二)：熱流力實驗』")
st.image("./imges/6.1.png", caption=" ")

st.markdown("**指導教授：** 周榮源")
st.markdown("**班級：** 四設計四甲")
st.markdown("**組別：** 第一組")
st.markdown("""**組員：** 
            41023120 呂昕叡
            41023124 李茂廷
            41023131 林承志
            41023142 姜陳昊
""")
st.markdown("**日期：** 113年12月24號")
# 壹、實驗目的
st.header("壹、實驗目的")
st.write("""真空抽氣之目的在造就一低壓力或極低壓力的空間，而所能達到之壓力視真空系統內氣 體負荷與真空幫浦抽氣速率大小而定，
         如果抽氣量大於氣體負荷，則系統壓力會逐漸降低， 直到兩者相等後，則系統維持在終極壓力而不再改變。""")

# 貳、儀器與設備
st.header("貳、儀器與設備")
st.image("./imges/6.2.png", caption="真空幫浦  ")
st.image("./imges/6.1.png", caption=" 腔體 ")
st.image("./imges/6.3.png", caption="真空值量測器 ")


# 參、實驗原理
st.header("參、實驗原理")
st.write("""
真空幫浦之功能是將一特定空間之氣體抽除，使氣體密度降低，達到某一壓力狀態。但 是，氣體在真空系統中之流動特性隨壓力之不同而有很大差異，如表1所示。因此，對不同 壓力範圍必須依相對應之抽氣原理來設計不同型態幫浦。
同時，針對特定抽氣要求，需組合 搭配不同性能與型態之真空幫浦來使用，才能達到有效又經濟之真空抽氣目的。圖1所示為 一真空系統基本架構，主要包括真空腔體、真空幫浦(粗抽幫浦及高真空幫浦)、真空計、抽 氣管路系統及壓力調節功能(製程氣體供氣、清洗、壓力控制)等。 
真空幫浦之抽氣速率(Pumping Speed)係指幫浦進氣口處之容積流率大小，其單位為L/s, m3/hr 等型式。在穩定抽氣狀態時，可由氣流通量(Throughput) Q及壓力P來決定，亦即S = Q/P。
單位時間內通過一導通面積單元之氣體質量稱為質量流率(Mass Flow Rate)，事實上與 氣流通量具有相同物理意義，但在真空技術中常以壓力及體積之乘積PV值，間接表示氣體 總質量G。
真空幫浦之抽氣量即進氣口處之氣流通量，其單位是Torr•L/s。如果進氣口壓力為 定值，則氣流通量可寫成Q = P × S。真空幫浦之抽氣量不同於抽氣速率，Q之大小較具實物理意義：
         氣體密度高時，壓力大，若密度與溫度為定值，則Q與S成正比；但是，在高真 空狀態下，氣體密度很稀薄，此時Q之大小較能表示真空幫浦真正性能，抽氣速率本身並不 足以完整顯示真空抽氣系統之工作效能。
 另一個常見的真空系統名詞為氣導(Conductance, C)，氣導之特性包含： 
(1) 其單位與抽氣速率相同； 
(2) 氣導大小決定於管路幾何形狀及氣壓； 
(3) 真空度高時，氣導與壓力無關。在中低真空度時，與壓力有密切關聯； 
(4) 由於真空系統中有許多孔、閥、管⋯等元件，會造成氣導降低，因此真空幫浦實際有效抽 氣速率(Seff ) 
可由下式求得
""")
st.image("./imges/6.6.png", caption=" ")
st.write("氣導大小可由Q = C(P1-P2 ) 關係式求得，在相同壓差下，氣流通量與氣導成正比。所以， 參考表1中氣導的計算式可知，選擇真空管路之原則是長度(L)要短，直徑(D)要大。")
st.image("./imges/6.4.png", caption=" ")
st.image("./imges/6.5.png", caption=" ")

# 肆、實驗步驟
st.header("肆、實驗步驟")
st.write("1.將閥門轉至全開(約20圈，每個人手徑不同)。")
st.image("./imges/6.2.png", caption=" ")
st.write("2. 將腔體蓋子蓋上，管路末端的出口開關關上，接著開啟幫浦，開始抽真空，一段時間後，可以嘗試打開蓋子(打不開的，如果打開了代表有出錯)。")
st.image("./imges/6.1.png", caption=" ")
st.write("3.開始觀察測量器上的數值，直到數值穩定，就將閥門準10圈至半開狀態，再重複1、2步驟，然後觀測數值。")
st.image("./imges/6.3.png", caption=" ")
st.write("4.	查看數據下圖為半開(最為穩定的數值)")
st.image("./imges/6.7.png", caption=" 半開")
st.write("下圖為全開(最為穩定的數值)")
st.image("./imges/6.8.png", caption=" 全開")

st.write("""
(有錄影上傳yt)
全開:
https://youtube.com/shorts/Yx-8dL7XaOs?feature=share 
半開:
https://youtu.be/yADPHbXCRBQ

""")

# 伍、實驗結果與討論
st.header("""伍、實驗結果與討論
          在真空技術中，真空數值越大，通常表示真空度越低（接近大氣壓）；相反，真空數值越小，則表示真空度越高（接近理論上的絕對真空）。以下是詳細解釋：""")
st.write("最終數值紀錄")
st.image("./imges/6.9.png", caption="數值表")
st.write("""
1. 真空等級的理解
•	高壓（低真空）： 當壓力值較大（例如 760 Torr，101.3 kPa）時，表示系統內的氣體較多，真空度較低，抽氣效果較弱。
•	低壓（高真空）： 當壓力值較小（例如 10⁻³ Torr，1 mPa）時，表示系統內的氣體較少，真空度較高，接近理想真空。

""")
st.write("""
2. 真空技術中的壓力單位
•	Torr（托）： 真空技術中常用單位，1 Torr ≈ 133.3 帕斯卡（Pa）。
•	帕斯卡（Pa）： 國際單位制壓力單位，真空工程中也常用。
•	Micron（微米汞柱）： 1 微米汞柱 = 0.001 Torr，用於非常細微的真空測量。

""")
st.write("""
例如：
•	大氣壓： 約 760 Torr 或 101,325 Pa。
•	中真空： 約 1 Torr 或 133.3 Pa。
•	高真空： 小於 10⁻³ Torr 或 0.133 Pa。
•	超高真空： 小於 10⁻⁹ Torr 或 10⁻⁷ Pa。

""")

# 參考文獻
st.header("參考文獻")
st.write("""
1.https://zh.wikipedia.org/zh-tw/%E7%9C%9F%E7%A9%BA
2.http://www.phys.nthu.edu.tw/~thschang/notes/VAC01.pdf
3.http://api.lib.ntnu.edu.tw:8080/server/api/core/bitstreams/c15ac3f8-c5ab-45a3-9844-ef8ee964c145/content

""")

