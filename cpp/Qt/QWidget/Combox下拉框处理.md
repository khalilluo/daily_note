```c++
void NewRPServer::dealComboxBox(QComboBox * dealcomboBox)
{
	dealcomboBox->setEditable(true);
	dealcomboBox->setFocusPolicy(Qt::NoFocus);
	QLineEdit *lineEditQ1 = dealcomboBox->lineEdit();
	lineEditQ1->setStyleSheet("QLineEdit{border-radius:1px;background-color:transparent;color: #000000;border:none;padding:0 0px;} \
		QLineEdit::disable{border-radius:1px;background-color:transparent;color: #000000;border:none;padding:0 0px;}");
	lineEditQ1->setFocusPolicy(Qt::NoFocus);
	lineEditQ1->setEnabled(false);
}
```