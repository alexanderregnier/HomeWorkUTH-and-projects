using System;
using System.Collections.Generic;
using MySql.Data.MySqlClient;
using System.IO;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ensambladora
{
    public partial class Form10 : Form
    {
        public Form10()
        {
            InitializeComponent();
        }

        string archivo = Directory.GetCurrentDirectory() + "\\ReporteVenComp.htm";

        private void button1_Click(object sender, EventArgs e)
        {
            StreamWriter arch = new StreamWriter(archivo);
            arch.WriteLine("<html>REPORTE DE VENTAS POR COMPONENTE<br><br>");
            arch.WriteLine("<table border=1 cellspacing=0>");
            arch.WriteLine("<tr><td>Componente</td><td>id_ventas</td></tr>");
            string connectionString = "datasource=localhost;port=3307;username=root;password=1234;database=ensambladora;";
            string query = "SELECT componente, total FROM Componentes JOIN(SELECT id_componen, COUNT(id_ventas) total FROM ventas GROUP BY id_componen) t ON Componentes.id_componen = t.id_componen;";
            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query, databaseConnection);
            MySqlDataReader reader;

            try
            {
                databaseConnection.Open();
                reader = commandDatabase.ExecuteReader();
                if (reader.HasRows)
                {
                    while (reader.Read())
                    {
                        arch.WriteLine("<tr><td>"
                        + reader.GetString(0) + "</td><td>" + reader.GetString(1) + "</td><td></tr>");
                    }
                }
                else
                {
                    MessageBox.Show("No se encontraron datos.");
                }
                databaseConnection.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            arch.WriteLine("</table></html>");
            arch.Close();
            Uri dir = new Uri(archivo);
            webBrowser1.Url = dir;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start("Excel", "\"" + archivo + "\"");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start("Opera", "\"" + archivo + "\"");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void Form10_Load(object sender, EventArgs e)
        {
            this.button4.Text = "Exit";
            this.button1.Text = "Generate";
            this.Text = "Sales Report by Component";
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }
    }
}
