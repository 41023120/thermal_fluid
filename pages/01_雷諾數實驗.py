import streamlit as st

st.title("實驗一: 雷諾數實驗")
# 在這裡添加實驗一的具體內容，如圖表、數據等
st.markdown("### 國立虎尾科技大學機械設計工程系")
st.markdown("### 113學年度『機械工程實驗(二)：熱流力實驗』")
st.image("./imges/1.29.png", caption="")
st.markdown("**指導教授：** 周榮源")
st.markdown("**班級：** 四設計四甲")
st.markdown("**組別：** 第一組")
st.markdown("""**組員：** 
            41023120 呂昕叡
            41023124 李茂廷
            41023131 林承志
            41023142 姜陳昊
""")
st.markdown("**日期：** 113年10月24號")
# 壹、實驗目的
st.header("壹、實驗目的")
st.write("　　以墨汁流入透明之壓克力管流中，觀察流體在管路中流動的情形，並配合計算出Re(雷諾數) ，以膫解層流和紊流與雷諾數(Re)之間的關係。")

# 貳、儀器與設備
st.header("貳、儀器與設備")
st.image("./imges/1.2.png", caption="圖一、雷諾數儀器")
st.image("./imges/1.3.png", caption="")
st.write("1	外套管直徑	150mm 2	內套管直徑	25mm")
st.write("本套儀器是由一透明之壓克力製內外雙套管、機架台座、點滴液瓶、進出口閥、洩水閥")
st.write("及溢水管等和管路連接而成，詳細構造如圖一所示。")
st.image("./imges/1.23.png", caption="")
st.image("./imges/1.4.png", caption="")
# 參、實驗原理
st.write("""由上可知，Re 為一無因次參數，亦即其值不因使用之單位系統不同而發生變化。
此參數之重要性乃在 Re 之大小與流體之流動情況是層流或擾流有關。
當雷諾數小時，流動形態成層狀或板狀運動，在巨觀下，其相鄰各層並無混合現象。
此時若將一細絲狀之染料注入其中，可看出此染料成一條線而不致散開，此即大家所熟知的層流，其流況如圖(2a)所示。
現若稍微加快流速，使 Re 稍微家大，吾人可發現此層狀流體在管路下游處成不穩定之擾動現象(圖 2b) ，此種上游層流，下游擾流之現象，稱為轉換區""")
st.image("./imges/1.24.png", caption="")
st.write("""現若再度加快流速，可發現整個流場呈擾動現象(圖 2c)，此即所謂的擾流。
一般而言，當 Re<2300 時，流場為層流，Re>4000 時為擾流，2300<Re<4000 時則為轉換區。
本實驗旨在使同學由實驗中觀察層流、擾流、轉換區流場之不同，且驗証雷諾數與流場間之關係。
在雷諾數之計算上，只要測得流量 Q 及管徑 D，則由 V = Q/A ，及已知之流體性質ρ及μ即可求得所需的 Re。""")
st.image("./imges/1.6.png", caption="")
st.image("./imges/1.7.png", caption="")
st.image("./imges/1.3.png", caption="")


# 肆、實驗步驟
st.header("肆、實驗步驟")
st.write("1.墨水加水稀釋（約 1：5）後裝入點滴液瓶內並裝置在儀器上端。")
st.image("./imges/1.8.png", caption="")
st.write("2.打開進水口閥及內管出水口閥，並將進出口流量控制在穩定流動狀態(即外管水位維持在某一固定位置不變)。")
st.image("./imges/1.9.png", caption="")
st.write("3.將墨水之控制閥打開讓墨水穩定的滴入套筒中。")
st.image("./imges/1.10.png", caption="")
st.write("4.觀察墨水於管路中流動的情形(層流、紊流或於臨界區域)同時用 量杯(或水筒)量取流量並 用碼錶確實測量時間(秒)將此等資料數據(流動情形、流量、測量時間)詳細計錄。")
st.image("./imges/1.25.png", caption="")
st.write("5.改變流量(由小到大)至少取五種不同的流量，以確實觀察由層流變化到完全紊流的情形。")
st.image("./imges/1.14.png", caption="")
st.image("./imges/1.15.png", caption="")
st.image("./imges/1.16.png", caption="")
st.image("./imges/1.17.png", caption="")
st.write("""6.實驗結束，將墨水關閉，且洗淨針頭後置淸水桶內，以免墨汁乾化，堵塞針孔，
同時開大進 水閥(出口閥維持略開)讓淸水充滿套筒內 部(此時會有多餘的水從溢水口流出)讓其自然循環 數分鐘將墨汁 淸洗掉。""")
st.image("./imges/1.18.png", caption="")
st.write("7.最後再將進水閥關閉，並打開出口閥和洩水閥將水排乾。")
st.image("./imges/1.19.png", caption="")
st.write("8.擦淨儀器本身及四周地板")
st.image("./imges/1.20.png", caption="")
# 伍、實驗結果與討論
st.header("伍、實驗結果與討論")
st.write("1.依實驗之觀察和計算結果，試判斷層流和紊流的臨界區域値在何種範圍。")
st.write("根據實驗的觀察結果與計算，層流和紊流的臨界區域值通常在雷諾數2300到4000之間。當雷諾數低於 2300 時流體主要呈現層流，而當雷諾數高於 4000 時流體變成紊流")
st.write("2.進出口端點處的不穩定現象原因")
st.write("進出口端點處的不穩定現象通常是由於流速突然變化或入口和出口端的邊界效應所引起的。進口處的流體由靜止狀態進入流動狀態，出口處因為擴散或外部壓力的改變，使流體在這些點處出現不穩定的擾動")
st.write("3.層流與紊流的流動情形繪圖及說明")
st.write("在層流中，水分子呈現層狀流動，彼此之間互不干擾，形成平行的流線。墨水在管道中呈現一條細長的線條，不會擴散開。在紊流中，水分子呈現混亂流動，流線互相干擾且呈現隨機運動。墨水在流動過程中會迅速擴散開，無法保持線狀")
st.write("4.實驗數據與書籍數據的符合性及改進建議")
st.write("若實驗結果與書籍中數據有所差異，可能原因包括儀器設備精度不足或流體黏度等實驗條件未達標準。改進建議為確保設備的精確度、提升數據測量的精密性，並在流量控制上做到更精確的穩定流動")
st.image("./imges/1.21.png", caption="")
st.image("./imges/1.22.png", caption="")
st.video("./imges/1.MOV")
# 參考文獻
st.header("柒、延伸應用與討論")
st.write("1. 列表整理出圓管、通道、矩(或方)形斷面管、任意形狀(如血管) 之 Re 算法，及在 Laminar flow ,transition flow, turbulent flow 下 Re 範圍?")
st.image("./imges/1.26.png", caption="")
st.write("2. 以一平板為例，外流場之 Re 算法(公式)? 在 Laminar flow, transition flow, turbulent flow 下之Re 範圍?")
st.image("./imges/1.27.png", caption="")
st.write("3. 請估算一下當你騎機車時，Re 在 Laminar flow, transition flow, turbulent flow 下相當速度是多快?")
st.image("./imges/1.28.png", caption="")


st.write("""
1. J.P. Holman,Experimental Methods for Engineers,McGRAW-Hill.
2. R.S. Figliola and D.F. Beasley,Theory and Design for Mechanical
   Measurement,Wiley.
3. E.R.G. Eckert and R.J. Goldstein, Measurements in Heat Transfer, Hemishpere  Publishing Co.

""")

