import streamlit as st
import pandas as pd
with st.sidebar:
    st.title('✌️导航菜单')
st.set_page_config(page_title="学生成绩分析平台", page_icon='💯')
page = st.sidebar.selectbox("选择页面", ["项目介绍", "专业数据分析", "成绩预测"])
if page=='项目介绍':
    st.title("🎓学生成绩分析与预测系统")

    b1,b2=st.columns(2)
    with b1:
        st.subheader("📋 项目概述")
        st.write("""
            本项目是一个基于Streamlit的学生成绩分析平台，通过数据可视化优化学习过程，
            帮助教育工作者和学生深入了解学业表现，并预测期末考试成绩。
            """)
        st.subheader("✨ 主要特点")
        st.markdown("""
        - 📊 **数据可视化**：多维度展示学生专业成绩
        - 📈 **专业分析**：按专业分类的统计与分析
        - 🤖 **智能预测**：基于学习模型的成绩预测
        - 🎯 **学习建议**：根据预测结果提供个性化改进
        """)
    with b2:
        images =[
            {
                 'url':"D:\\streamlit_env\\1.png",
                 'parm':'各专业性别分布分析'
             },
            {
                 'url':"D:\\streamlit_env\\2.png",
                 'parm':'各专业核心学习指标对比'
            },
            {
                 'url':"D:\\streamlit_env\\3.png",
                  'parm':'各专业上课出勤率分布'
            },
            {
                 'url':"D:\\streamlit_env\\4.png",
                 'parm':'大数据管理专业专项分析'
            }
        ]
    #讲ind的值存储到streamlit的内存中，如果内存中没有ind,才要设置成0，否则不需要设置
        if 'ind'not in st.session_state:
            st.session_state['ind']=0



    #define:定义
        def nextImg():
            st.session_state['ind']=(st.session_state['ind']+1) % len(images)
        def prevImg():
            st.session_state['ind']=(st.session_state['ind']-1) % len(images)

    #st.image()总共两个参数，url:图片地址 caption:图片的备注
        st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['parm'])

    #将一行分成两列
        c1,c2=st.columns(2)

        with c1:
        #st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
            st.button('上一张',on_click=prevImg,use_container_width=True)
        with c2:    
    #st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
            st.button('下一张',on_click=nextImg,use_container_width=True)



    st.markdown('------')
    st.subheader("🎯 项目目标")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("### 目标一\n- 分析影响学习因素\n- 识别关键薄弱点\n- 提供改进对策")
    with c2:
        st.markdown("### 目标二\n- 专业对比分析\n- 趋势差异研究\n- 学习模式识别")
    with c3:
        st.markdown("### 目标三\n- 预测学习趋势\n- 个性化建议\n- 及时干预预警")


    st.markdown('------')
    st.subheader("🔧 技术架构")
    a1, a2, a3 = st.columns(3)
    with a1:
        frontend_framework = st.text_input("前端框架", value="streamlit")  # 默认值为streamlit
    with a2:
        data_processing = st.text_area("数据处理", value="pandas\nnumpy", height=80)
    with a3:
        visualization = st.text_input("可视化", value="matplotlib plotly")

elif page == "专业数据分析":
    import streamlit as st
    st.set_page_config(page_title="专业数据分析",layout="wide", page_icon="📊")
    st.title("📊专业数据分析")

    import pandas as pd
    pd.set_option('display.unicode.east_asian_width',True)
    def load_data():
        # 确保CSV文件和代码在同一文件夹，文件名要写全（包含.csv后缀）
        df = pd.read_csv("student_data_adjusted_rounded.csv", encoding="utf-8")
        return df

    # 执行数据读取，定义df变量
    df = load_data()



    import streamlit as st
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots


    st.subheader("1.各专业性别分布分析👩‍❤️‍💋‍👨")

    # 1. 统计数据
    gender_by_major = df.groupby(["专业", "性别"]).size().reset_index(name="人数")
    gender_count = df.groupby(["专业", "性别"]).size().unstack(fill_value=0)
    gender_count["总人数"] = gender_count.sum(axis=1)
    gender_count["男生占比(%)"] = (gender_count["男"] / gender_count["总人数"] * 100).round(1)
    gender_count["女生占比(%)"] = (gender_count["女"] / gender_count["总人数"] * 100).round(1)
    gender_table = gender_count[["总人数", "男", "男生占比(%)", "女", "女生占比(%)"]].reset_index()
    gender_table.columns = ["专业", "总人数", "男生数", "男生占比(%)", "女生数", "女生占比(%)"]

    # 2. 分栏展示：左图表，右表格
    col1, col2 = st.columns([1.2, 1])  # 调整列宽比例
    with col1:
        # 双层柱状图
        fig_gender = px.bar(
            gender_by_major,
            x="专业",
            y="人数",
            color="性别",
            barmode="group",
            title="各专业男女人数分布",
            color_discrete_map={"男": "#1f77b4", "女": "#ff7f0e"}
        )
        fig_gender.update_traces(hovertemplate="专业：%{x}<br>性别：%{color}<br>人数：%{y}")
        st.plotly_chart(fig_gender, use_container_width=True)
    with col2:
        st.write('性别分布数据')
        # 性别比例表格
        st.dataframe(
            gender_table,
            use_container_width=True,
            hide_index=True,
            column_config={
                "男生占比(%)": st.column_config.NumberColumn(format="%.1f%%"),
                "女生占比(%)": st.column_config.NumberColumn(format="%.1f%%")
            }
        )



    st.markdown('------')
    with st.container():
        st.subheader("2. 各专业核心学习指标对比")
        col3,col4=st.columns([0.7,0.3])
        with col3:
            # 计算各专业关键指标均值
            prof_metrics = df.groupby("专业").agg({
                "每周学习时长（小时）": "mean",
                "上课出勤率": "mean",
                "期末考试分数": "mean"
            }).round(2)
            # 重置索引便于Plotly调用
            prof_metrics = prof_metrics.reset_index()
            # 数据重塑：将多指标转为长格式
            prof_metrics_melt = pd.melt(
                prof_metrics,
                id_vars="专业",
                value_vars=["每周学习时长（小时）", "上课出勤率", "期末考试分数"],
                var_name="指标类型",
                value_name="指标均值"
            )
            # 绘制分组柱状图
            fig_metrics = px.bar(
            prof_metrics_melt,
            x="专业",
            y="指标均值",
            color="指标类型",
            barmode="group",
            title="各专业学习指标均值对比（学习时长/出勤率/期末分数）",
            labels={"专业": "专业名称", "指标均值": "指标平均值"}
        )

        # 提取“期末考试分数”数据，添加折线图（以“专业”为x，“期末考试分数”为y）
            exam_scores = prof_metrics[["专业", "期末考试分数"]]
            fig_metrics.add_trace(
                go.Scatter(
                    x=exam_scores["专业"],
                    y=exam_scores["期末考试分数"],
                    mode="lines+markers",  # 折线+标记点
                    name="期末分数（折线）",
                    yaxis="y2",  # 绑定到右侧Y轴
                    line=dict(color="red", width=3)
                )
            )

            # 配置双Y轴（避免条形图和折线图数据范围冲突）
            fig_metrics.update_layout(
                xaxis_tickangle=45,
                yaxis=dict(title="学习时长/出勤率（左侧Y轴）"),
                yaxis2=dict(
                    title="期末分数（右侧Y轴）",
                    overlaying="y",  # 与左侧Y轴重叠
                    side="right"     # 显示在右侧
                )
            )

        # 渲染图表
            st.plotly_chart(fig_metrics, use_container_width=True)
        with col4:
            st.write("学习指标详细数据表格")
            st.dataframe(
                prof_metrics,  # 数据源为计算好的prof_metrics
                use_container_width=True,
                column_config={  # 可自定义列格式
                    "每周学习时长（小时）": st.column_config.NumberColumn(format="%.2f"),
                    "上课出勤率": st.column_config.NumberColumn(format="%.2f"),
                    "期末考试分数": st.column_config.NumberColumn(format="%.1f")
                }
            )




    st.markdown('------')
    with st.container():
        st.subheader("3. 各专业上课出勤率分布")
        col5,col6=st.columns([0.7,0.3])
        with col5:
            # 计算各专业出勤率均值（保留2位小数）
            attendance_prof = df.groupby("专业")["上课出勤率"].mean().round(3).reset_index()
            attendance_prof["上课出勤率"] = attendance_prof["上课出勤率"] * 100  # 转为百分比
            # 绘制彩色柱状图（按出勤率数值着色）
            fig_attendance = px.bar(
                attendance_prof,
                x="专业",
                y="上课出勤率",
                color="上课出勤率",
                color_continuous_scale=px.colors.sequential.Reds,
                title="各专业上课出勤率（%）",
                labels={"专业": "专业名称", "上课出勤率": "出勤率（%）"}
            )
            fig_attendance.update_layout(xaxis_tickangle=45)
            st.plotly_chart(fig_attendance, use_container_width=True)
        with col6:
            st.write("出勤率排名")
            st.dataframe(attendance_prof, use_container_width=True)


    st.markdown('------')
    st.subheader("4.大数据管理专业专项分析")
    bigdata_df = df[df["专业"] == "大数据管理"]
        # 顶部指标卡片
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("专业出勤率", f"{bigdata_df['上课出勤率'].mean()*100:.1f}%")
    with col2:
        st.metric("平均成绩", f"{(bigdata_df['期中考试分数']+bigdata_df['期末考试分数']).mean()/2:.1f}分")
    with col3:
        st.metric("作业完成率", f"{bigdata_df['作业完成率'].mean()*100:.1f}%")
    with col4:
        st.metric("平均每周学习时长", f"{bigdata_df['每周学习时长（小时）'].mean():.1f}小时")
        
        # 下方细分图表
    import numpy as np  # 导入numpy库，用于生成数据
    from scipy.stats import gaussian_kde  # 改用scipy的核密度函数
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:

    # 1. 读取数据并筛选“大数据管理”专业
        df = pd.read_csv("student_data_adjusted_rounded.csv")
        bigdata_scores = df[df["专业"] == "大数据管理"]["期末考试分数"].dropna()  # 过滤空值

        # 2. 计算核密度（用scipy实现）
        kde = gaussian_kde(bigdata_scores)
        x_vals = np.linspace(bigdata_scores.min(), bigdata_scores.max(), 100)  # 生成X轴取值
        y_vals = kde(x_vals)  # 计算对应密度

        # 3. 绘制直方图
        fig = px.histogram(
            x=bigdata_scores,
            nbins=10,
            histnorm="probability density",
            title="大数据管理专业期末成绩分布",
            labels={"x": "期末分数", "y": "密度"},
            opacity=0.7,
            color_discrete_sequence=["#2E8B57"]
        )

        # 4. 添加核密度曲线（用scipy计算的结果）
        fig.add_trace(go.Scatter(
            x=x_vals,
            y=y_vals,
            mode="lines",
            line=dict(color="#FF6347", width=2),
            name="核密度曲线"
        ))

        # 5. 配置布局
        fig.update_layout(
            plot_bgcolor="white",
            xaxis_range=[30, 100],
            xaxis_title="期末分数",
            yaxis_title="分布密度"
        )

        # 6. 显示图表
        st.plotly_chart(fig, use_container_width=True)

    with col_chart2:
        fig_box = px.box(bigdata_df, y="期末考试分数", title="期末成绩分布", color_discrete_sequence=["#2ecc71"])
        st.plotly_chart(fig_box, use_container_width=True)
    

else:
    import streamlit as st
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    import numpy as np
    from datetime import datetime, time


    # 页面配置
    st.set_page_config(page_title="期末成绩预测", layout="wide", page_icon="🥇")
    st.title("期末成绩预测")
    st.markdown("---")

    # 读取数据
    df = pd.read_csv("student_data_adjusted_rounded.csv")

    # 分栏布局
    c1, c2 = st.columns([1, 2])

    with c1:
        st.subheader("📍学号")
        student_id = st.selectbox("学号", df["学号"].unique())

        st.subheader("👤 性别")
        gender = st.selectbox(
            "选择性别",
            ["男", "女"],
            label_visibility='collapsed'
        )

        st.subheader("🎓 专业")
        major = st.selectbox(
            "请选择你的专业",
            ["工商管理", "人工智能", "财务管理", "电子商务", "大数据管理"],
            label_visibility='collapsed'
        )


    with c2:
        # 3. 训练成绩预测模型
        def train_pred_model():
            # 选择特征与目标列
            X = df[["每周学习时长（小时）", "上课出勤率", "期中考试分数", "作业完成率"]]
            y = df["期末考试分数"]
            # 训练线性回归模型
            model = LinearRegression()
            model.fit(X, y)
            return model

        model = train_pred_model()

        # 4. 输入表单区域
        st.subheader("输入学生学习信息")
        with st.form("pred_form"):
            # 输入特征（支持手动修改）
            hours = st.slider(
                "每周学习时长（小时）",
                10, 30,
                key="hours"
            )

            attendance = st.slider(
                "上课出勤率",
                0.6, 1.0,
                key="attendance"
            )

            mid_score = st.slider(
                "期中考试分数",
                40, 100,
                key="mid_score"
            )

            homework_rate = st.slider(
                "作业完成率",
                0.5, 1.0,
                key="homework_rate"
            )

            submit_btn = st.form_submit_button("提交预测")

            if submit_btn:
                # 构建输入特征
                input_features = np.array([[hours, attendance, mid_score, homework_rate]])
                # 模型预测
                try:
                    pred_score = model.predict(input_features)[0].round(2)
                except Exception as e:
                    st.error(f"预测失败：{str(e)}")
                    pred_score = 0

                # 显示预测结果
                st.subheader("预测结果")
                st.success(f"预测期末成绩：{pred_score} 分")

                # 显示祝贺图（成绩达标时）
                if pred_score >= 80:
                    st.image("https://p2.itc.cn/q_70/images03/20230425/b1f37db99ccd451aac4f948bf477404d.png", use_container_width=True)  # 替换为实际图片路径
                    st.markdown("**学习建议：保持当前状态，继续巩固知识！**")
                else:
                    st.image("https://img.coozhi.com/upload/20200609/o15a91e69786ue12fe2d02387e05a1c5a5e90adf5a069dd.0x750x450.jpg", use_container_width=True)
                    st.warning("建议增加学习时长，提升课堂参与度")
