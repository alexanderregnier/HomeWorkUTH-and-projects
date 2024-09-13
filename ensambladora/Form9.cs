using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using MySql.Data.MySqlClient;
using System.IO;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ensambladora
{
    public partial class Form9 : Form
    {
        public Form9()
        {
            InitializeComponent();
        }

        string archivo = Directory.GetCurrentDirectory() + "\\ReporteVenCli.htm";

        private void button1_Click(object sender, EventArgs e)
        {
            StreamWriter arch = new StreamWriter(archivo);
            arch.WriteLine("<html><meta charset=\"utf-8\">REPORTE DE VENTAS POR CLIENTE<br><br>");
            arch.WriteLine("<table border=1 cellspacing=0>");
            arch.WriteLine("<tr><td>cliente</td><td>id_ventas</td></tr>");
            string connectionString = "datasource=localhost;port=3307;username=root;password=1234;database=ensambladora;";
            string query = "SELECT cliente, total FROM clientes JOIN(SELECT Id_cliente, COUNT(id_ventas) total FROM ventas GROUP BY Id_cliente) t ON clientes.Id_cliente = t.Id_cliente;";
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

        private void Form9_Load(object sender, EventArgs e)
        {
            if (Form1.idioma == "2")
            {
                this.button1.Text = "Generate";
                this.button4.Text = "Exit";
            }
        }
    }
}
