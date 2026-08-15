import QtQuick
import QtQuick.Layouts
import org.kde.plasma.plasma5support as Plasma5Support
import org.kde.plasma.plasmoid
import org.kde.kirigami as Kirigami

PlasmoidItem {
    id: root

    property int allowed: 0
    property int blocked: 0
    property int total: 0
    property real percentage: 0
    property string updated: "--:--:--"
    property string errorMsg: ""

    Plasma5Support.DataSource {
        id: statsData
        engine: "executable"
        connectedSources: [
            Qt.resolvedUrl("../../read-stats.sh").toString().replace("file://", "")
        ]
        interval: 62000

        onNewData: function(sourceName, data) {

            try {
                var stdout = String(data["stdout"] || "")

                var json = JSON.parse(stdout)

                root.allowed = json.allowed
                root.blocked = json.blocked
                root.total = json.total
                root.percentage = json.percentage
                root.updated = json.updated || "--:--:--"
                root.errorMsg = ""
            } catch (e) {
                root.errorMsg = "JSON Parse Error"
            }
        }
    }

    preferredRepresentation: fullRepresentation

    fullRepresentation: Item {
        implicitWidth: 280
        implicitHeight: 190

        ColumnLayout {
            anchors.left: parent.left
            anchors.leftMargin: 20
            anchors.verticalCenter: parent.verticalCenter
            spacing: 10

            RowLayout {
                Kirigami.Icon {
                    source: "network-server"
                    Layout.preferredWidth: 28
                    Layout.preferredHeight: 28
                }

                Text {
                    text: "NextDNS"
                    font.pixelSize: 20
                    font.bold: true
                    color: Kirigami.Theme.textColor
                }
            }

            Text {
                text: root.errorMsg ? "⚠️ " + root.errorMsg : ""
                color: "red"
                visible: root.errorMsg !== ""
            }

            RowLayout {
                Kirigami.Icon {
                    source: "dialog-ok"
                    Layout.preferredWidth: 20
                    Layout.preferredHeight: 20
                }

                Text {
                    text: "Allowed"
                    Layout.preferredWidth: 80
                    color: Kirigami.Theme.textColor
                }

                Text {
                    text: root.allowed
                    font.bold: true
                    color: Kirigami.Theme.textColor
                }
            }

            RowLayout {
                Kirigami.Icon {
                    source: "dialog-error"
                    Layout.preferredWidth: 20
                    Layout.preferredHeight: 20
                }

                Text {
                    text: "Blocked"
                    Layout.preferredWidth: 80
                    color: Kirigami.Theme.textColor
                }

                Text {
                    text: root.blocked
                    font.bold: true
                    color: Kirigami.Theme.textColor
                }
            }

            RowLayout {
                Kirigami.Icon {
                    source: "view-statistics"
                    Layout.preferredWidth: 20
                    Layout.preferredHeight: 20
                }

                Text {
                    text: "Total"
                    Layout.preferredWidth: 80
                    color: Kirigami.Theme.textColor
                }

                Text {
                    text: root.total
                    font.bold: true
                    color: Kirigami.Theme.textColor
                }
            }

            ColumnLayout {
                RowLayout {
                    Kirigami.Icon {
                        source: "office-chart-pie"
                        Layout.preferredWidth: 20
                        Layout.preferredHeight: 20
                    }

                    Text {
                        text: "Blocked rate"
                        Layout.preferredWidth: 80
                        color: Kirigami.Theme.textColor
                    }

                    Text {
                        text: root.percentage.toFixed(2) + "%"
                        font.bold: true
                        color: Kirigami.Theme.textColor
                    }
                }

                Item {
                    Layout.preferredWidth: 220
                    Layout.preferredHeight: 20

                    Rectangle {
                        anchors.verticalCenter: parent.verticalCenter
                        width: 180
                        height: 8
                        radius: 4
                        color: "#404040"

                        Rectangle {
                            width: parent.width * (root.percentage / 100)
                            height: parent.height
                            radius: parent.radius
                            color: "#4CAF50"
                        }
                    }
                }

                RowLayout {
                    Kirigami.Icon {
                        source: "view-refresh"
                        Layout.preferredWidth: 20
                        Layout.preferredHeight: 20
                    }

                    Text {
                        text: "Updated"
                        Layout.preferredWidth: 80
                        color: Kirigami.Theme.textColor
                    }

                    Text {
                        text: root.updated
                        font.bold: true
                        color: Kirigami.Theme.textColor
                    }
                }
            }
        }
    }
}
