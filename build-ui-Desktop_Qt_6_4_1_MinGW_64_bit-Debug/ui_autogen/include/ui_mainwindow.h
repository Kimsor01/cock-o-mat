/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.4.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_cockomat
{
public:
    QWidget *centralwidget;
    QListWidget *listDrinkSelection;
    QListWidget *listDrinkDetails;
    QPushButton *pbOptions;
    QPushButton *pbPourDrink;
    QComboBox *cbTypes;
    QPushButton *pbFart;
    QPushButton *pbRandom;
    QPushButton *pbShowAll;
    QLabel *labelDrink;

    void setupUi(QMainWindow *cockomat)
    {
        if (cockomat->objectName().isEmpty())
            cockomat->setObjectName("cockomat");
        cockomat->setWindowModality(Qt::NonModal);
        cockomat->setEnabled(true);
        cockomat->resize(800, 480);
        cockomat->setMaximumSize(QSize(800, 480));
        cockomat->setBaseSize(QSize(800, 480));
        QFont font;
        font.setFamilies({QString::fromUtf8("Arial")});
        font.setPointSize(11);
        font.setKerning(true);
        font.setStyleStrategy(QFont::PreferDefault);
        cockomat->setFont(font);
        cockomat->setAcceptDrops(false);
        centralwidget = new QWidget(cockomat);
        centralwidget->setObjectName("centralwidget");
        listDrinkSelection = new QListWidget(centralwidget);
        listDrinkSelection->setObjectName("listDrinkSelection");
        listDrinkSelection->setGeometry(QRect(10, 67, 320, 381));
        listDrinkSelection->setFrameShape(QFrame::StyledPanel);
        listDrinkSelection->setFrameShadow(QFrame::Sunken);
        listDrinkSelection->setLineWidth(1);
        listDrinkSelection->setMidLineWidth(0);
        listDrinkSelection->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        listDrinkSelection->setSizeAdjustPolicy(QAbstractScrollArea::AdjustIgnored);
        listDrinkSelection->setEditTriggers(QAbstractItemView::NoEditTriggers);
        listDrinkSelection->setProperty("showDropIndicator", QVariant(false));
        listDrinkSelection->setDefaultDropAction(Qt::IgnoreAction);
        listDrinkSelection->setAlternatingRowColors(true);
        listDrinkSelection->setSortingEnabled(true);
        listDrinkDetails = new QListWidget(centralwidget);
        listDrinkDetails->setObjectName("listDrinkDetails");
        listDrinkDetails->setGeometry(QRect(470, 107, 320, 291));
        pbOptions = new QPushButton(centralwidget);
        pbOptions->setObjectName("pbOptions");
        pbOptions->setGeometry(QRect(760, 10, 30, 30));
        pbPourDrink = new QPushButton(centralwidget);
        pbPourDrink->setObjectName("pbPourDrink");
        pbPourDrink->setGeometry(QRect(660, 420, 121, 31));
        cbTypes = new QComboBox(centralwidget);
        cbTypes->setObjectName("cbTypes");
        cbTypes->setGeometry(QRect(90, 10, 79, 25));
        cbTypes->setInsertPolicy(QComboBox::InsertAlphabetically);
        cbTypes->setSizeAdjustPolicy(QComboBox::AdjustToContents);
        cbTypes->setDuplicatesEnabled(false);
        pbFart = new QPushButton(centralwidget);
        pbFart->setObjectName("pbFart");
        pbFart->setGeometry(QRect(350, 130, 80, 24));
        pbRandom = new QPushButton(centralwidget);
        pbRandom->setObjectName("pbRandom");
        pbRandom->setGeometry(QRect(350, 90, 77, 25));
        pbRandom->setCheckable(true);
        pbShowAll = new QPushButton(centralwidget);
        pbShowAll->setObjectName("pbShowAll");
        pbShowAll->setGeometry(QRect(10, 10, 77, 25));
        pbShowAll->setTabletTracking(false);
        pbShowAll->setCheckable(false);
        pbShowAll->setChecked(false);
        labelDrink = new QLabel(centralwidget);
        labelDrink->setObjectName("labelDrink");
        labelDrink->setGeometry(QRect(470, 80, 311, 16));
        QFont font1;
        font1.setFamilies({QString::fromUtf8("Arial")});
        font1.setPointSize(13);
        font1.setBold(true);
        font1.setKerning(true);
        font1.setStyleStrategy(QFont::PreferDefault);
        labelDrink->setFont(font1);
        labelDrink->setFrameShape(QFrame::NoFrame);
        labelDrink->setAlignment(Qt::AlignCenter);
        labelDrink->setTextInteractionFlags(Qt::NoTextInteraction);
        cockomat->setCentralWidget(centralwidget);

        retranslateUi(cockomat);

        QMetaObject::connectSlotsByName(cockomat);
    } // setupUi

    void retranslateUi(QMainWindow *cockomat)
    {
        cockomat->setWindowTitle(QCoreApplication::translate("cockomat", "Cock-o-mat", nullptr));
        pbOptions->setText(QCoreApplication::translate("cockomat", "x", nullptr));
        pbPourDrink->setText(QCoreApplication::translate("cockomat", "PushButton", nullptr));
        pbFart->setText(QCoreApplication::translate("cockomat", "Fart", nullptr));
        pbRandom->setText(QCoreApplication::translate("cockomat", "Zufall", nullptr));
        pbShowAll->setText(QCoreApplication::translate("cockomat", "Alle", nullptr));
        labelDrink->setText(QCoreApplication::translate("cockomat", "TextLabel", nullptr));
    } // retranslateUi

};

namespace Ui {
    class cockomat: public Ui_cockomat {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
