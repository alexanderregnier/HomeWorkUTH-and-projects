using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using MySql.Data.MySqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ensambladora
{
    public partial class Form8 : Form
    {
        public Form8()
        {
            InitializeComponent();
        }

        string archivo = Directory.GetCurrentDirectory() + "\\ReporteComponentes.htm";

        private void button1_Click(object sender, EventArgs e)
        {
            StreamWriter arch = new StreamWriter(archivo);
            arch.WriteLine("<html>REPORTE DE COMPONENTES<br><br>");
            arch.WriteLine("<table border=1 cellspacing=0>");
            arch.WriteLine("<tr><td>id_componente</td><td>componente</td><td>precio</td><td>Disponible</td></tr>");
            string connectionString = "datasource=localhost;port=3307;username=root;password=1234;database=ensambladora;";
            string query = "Select * from Componentes";
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
                        + reader.GetString(0) + "</td><td>" + reader.GetString(1) + "</td><td>"
                        + reader.GetString(2) + "</td><td>" + reader.GetString(3) + "</td></tr>");
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

        private void Form8_Load(object sender, EventArgs e)
        {
            if (Form1.idioma == "2")
            {
                this.button1.Text = "Generate";
                this.button4.Text = "Exit";
            }
        }
    }
}
