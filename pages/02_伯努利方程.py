import streamlit as st

st.title("實驗二: 水衝擊實驗")
# 在這裡添加實驗一的具體內容，如圖表、數據等
st.markdown("### 國立虎尾科技大學機械設計工程系")
st.markdown("**指導教授：** 周榮源")
st.markdown("**班級：** 四設計四甲")
st.markdown("**組別：** 第一組")
st.markdown("**組員：** 呂昕叡, 李茂廷, 林承志, 姜陳昊")
st.markdown("**日期：** 105年10月24號")
# 壹、實驗目的
st.header("壹、實驗目的")
st.write("瞭解流體流動時，其動量變化與其承受力量間之關係，以驗証動量方程式。")

# 貳、儀器與設備
st.header("貳、儀器與設備")
  # 請替換為實際圖片路徑
st.write("""水衝擊實驗係由一水循環泵、驅動馬達、儲水槽、實驗台架、柏登壓力錶、流量控制閥、水衝擊台一套(包括有透明壓克力套筒、噴嘴、各種形式之衝擊檔板、動量平衡器)、以及三角形堰(流量計)、和稱重器等構成整套儀器，詳細構造如圖一所示。
""")
st.image("C:\\Users\\luxui\\thermal_fluid\\pages\\images\\2-1.png", caption=" ")
st.image("C:\\Users\\luxui\\thermal_fluid\\pages\\images\\2-2.png", caption=" ")
st.image("C:\\Users\\luxui\\thermal_fluid\\pages\\images\\2-3.png", caption=" ")
# 參、實驗原理
st.header("參、實驗原理")
st.write("衝擊試驗之主要目的在驗証動量方程式。吾人知道動量方程式屬於流體力學四大方程式之一，其應用頗為廣泛，如衝動式水輪機之分析、各型彎管、噴嘴之受力分析等均有賴動量方程式的計算。至於各式離心泵、衝動式水輪機等亦需藉重經由動量方式推導出之動量矩方程式來分析，故吾人希望藉重此一實驗來加深讀者對動量方程式應用在流體力學的控制體積時，一般可表為下列之形式")
st.image("C:\\Users\\luxui\\thermal_fluid\\pages\\images\\2-4.png", caption=" ")
st.image("C:\\Users\\luxui\\thermal_fluid\\pages\\images\\2-5.png", caption=" ")
st.image("C:\\Users\\luxui\\thermal_fluid\\pages\\images\\2-6.png", caption=" ")
st.write("即 X 方向之受力=流出之動量在 X 方向之分量 – 流入之動量在 X 方向之分量其他 y、z方向之情形均同，在此不再重複。為了驗證此一動量方程式，及加強同學對動量方程式的瞭解，本實驗設計了三種不同形狀的硯板，其理論上之受力情形，可用上面所述之簡單理論加以推導之。在推導其基本方程式的時候，吾人均做了如下的假設:")
st.write("""
1.平板之表面極為光滑，可視為無磨擦，即水進入平板之速度 Vj 等於流出平板之速度 Ve。
2.因水之重力對平板產生之影響很小，故予以忽略。
3.穩定流。
""")
st.image("C:\\Users\\luxui\\thermal_fluid\\pages\\images\\2-7.png", caption=" ")
st.image("C:\\Users\\luxui\\thermal_fluid\\pages\\images\\2-8.png", caption=" ")
st.image("C:\\Users\\luxui\\thermal_fluid\\pages\\images\\2-9.png", caption=" ")
st.image("C:\\Users\\luxui\\thermal_fluid\\pages\\images\\2-10.png", caption=" ")
# 若有更多公式或數據表，可以插入 st.latex 或 st.dataframe 來呈現
st.image("C:\\Users\\luxui\\thermal_fluid\\pages\\images\\2-11.png", caption=" ")

# 肆、實驗步驟
st.header("肆、實驗步驟")
st.write("""
1.	將 110V 之電源連接妥當。
2.	儲水槽加入之水量約九分滿。
3.	將噴嘴及硯板裝入水衝擊器內。
4.	將動量平衡器先預加上荷重約 350～450gms，使其壓縮彈簧約 80%之壓縮量(勿將彈簧完全壓縮，否則會產生很大的誤差〉，並將平衡指標切口對準與平板同高，此時需將試重之實際重量［包括容器、即杯子 ］計錄下來，此即為預負荷。
5.	按下啟動馬達開關，並逐漸打開流量控制閥至某一特定流量。
6.	同時衝擊水流對硯板產生衝擊，而將硯板上推至最高點。此時開始加入荷重，至平板回到原來之平衡位置為止，取下容杯重新稱重，即得總負荷。總負荷減去預負荷，所得之重量即為水對硯板之衝擊力。
7.	逐漸打開流量控制閥（出口閥），以改變流量，重覆上述步驟，流量由小至大，至少取五種，並詳細記錄各值。
8.	關閉電源，並將出口閥關閉。
9.	依序更換噴嘴或硯扳，重覆 3～8 之步驟完成同樣之量測。
10.	實驗結束，關閉電源，並將流量測量槽內之水排放至儲水槽。

""")
st.image("C:\\Users\\luxui\\thermal_fluid\\pages\\images\\2-13.png", caption=" ")
st.image("C:\\Users\\luxui\\thermal_fluid\\pages\\images\\2-14.png", caption=" ")
st.image("C:\\Users\\luxui\\thermal_fluid\\pages\\images\\2-15.png", caption=" ")
st.image("C:\\Users\\luxui\\thermal_fluid\\pages\\images\\2-16.png", caption=" ")
st.image("C:\\Users\\luxui\\thermal_fluid\\pages\\images\\2-17.png", caption=" ")
st.image("C:\\Users\\luxui\\thermal_fluid\\pages\\images\\2-18.png", caption=" ")
# 伍、實驗結果與討論
st.header("伍、實驗結果與討論")
st.write("""
1.	討論硯板與噴嘴間之距離對硯板受力大小之影響。
       答:根據水衝擊實驗原理，噴嘴與硯板的距離會影響水流的擴散程度。當距離增加時，水流擴散更廣，可能導致水的速度減小，因而降低硯板所受的衝擊力。相反，距離較近時，水流衝擊集中在硯板表面，受力更大。因此，噴嘴與硯板之間的距離直接影響硯板的受力大小
2.	討論在同流量之情況下，噴嘴直徑與硯板受力之關係。
       答:在同流量的情況下，較小的噴嘴直徑會導致水流速度增加，根據動量方程式，較快的水流會產生更大的動量，進而增強衝擊力。因此，使用5mm直徑噴嘴會比8mm直徑噴嘴產生更大的衝擊力
3.	繪製流速與硯板受力之關係圖，比較三種硯板之受力情形。
       答:根據實驗數據，隨著流速增加，硯板所受的衝擊力也增加。然而，三種硯板（平板、45度錐形、半球形）的受力大小不同。實驗結果顯示，在相同流速下，半球形硯板因水流折返效果，受力最大，而平板受力相對較小。圖表可呈現三種硯板受力隨流速增加的趨勢
4.	討論誤差大小與噴嘴直徑、硯板形狀間之關係。
       答:誤差大小與噴嘴直徑和硯板形狀有顯著關係。較小的噴嘴直徑（例如5mm）因水流集中，測量結果較為穩定，誤差較小。而不同形狀的硯板會因表面特性和流體方向改變而導致測量誤差的差異。例如，半球形硯板因水流折返，較容易產生不穩定的測量結果，因此誤差可能較大
""")
st.header("陸、測驗題")
st.write("""
1.	水衝擊實驗在驗証柏努利、雷諾方程式。
2.	本實驗有哪幾種硯板可供實驗：水平 圓錐形 半圓形
3.	本實驗有那幾種規格之噴嘴： 8mm	、5mm。
4 在流量固定之下,使用同一硯板,配合那一個噴嘴衝擊力較大5mm ,為什麼：噴嘴口徑較小的5mm噴嘴會使水流速度增加，從而提高動量。根據動量方程式，水流速度越快，對目標物的衝擊力越大。。
5.	在同一流量和噴嘴,那一種硯板衝擊力最大8mm ,水平硯板衝擊力最小,最大約爲最小的1.47倍。
6.	在流量固定下何種噴嘴與硯板之組合衝擊力最大：5mm水平硯板 ,何種組合衝擊力最小：8mm	 , 水平硯板。前者 約爲後者的1.47倍。 7.1Kgw=	N。
8.	推導 ρQV 所得到之單位：牛頓(N)。〈取 ρ 爲 kg/m3,Q 爲m3/s, V 爲m/s〉

9.	預負荷 300gw,總負荷 2800gw,Q=30l /min ,噴嘴 5mm 作用在半圓形硯板,則實際負荷為	24.53N ,理論衝擊力162.11N,誤差爲84.87％。


""")
# 參考文獻
st.header("參考文獻")
st.write("""
1.	J.P. Holman, Experimental Methods for Engineers, McGRAW-Hill.
2.	R.S. Figliola and D.F. Beasley, Theory and Design for Mechanical Measurement, Wiley.
3.	E.R.G. Eckert and R.J. Goldstein, Measurements in Heat Transfer, Hemishpere Publishing Co.

""")

