

### QWidget

- 普通控件启动drag是在mouse时间里面new QDrag，传递QMimeData。启动条件可以依据拖动距离的ManhattanLength(**直角三角形直角边之和**)
- 接收drop的控件需要设置accetpDrop属性，然后在dragEnter时AcceptProposedAction才能收到Drop事件

#### QTableWidget

- 表格直接acceptDrop的话无法收到Drop事件，需要把AcceptDrop放到背景控件或者viewPort()
- dragDropMode设置为NoDragDrop，手动设置数据比较可控
- eventFilter里面出现两次drop的事件可能是因为没有讲drop事件处理（return true）导致
- 如果表格直接acceptDrop接收其他表格的拖动的话会出现表格内容的拖动复制
