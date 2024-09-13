using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using MySql.Data.MySqlClient;

namespace ensambladora
{
    public partial class Form14 : Form
    {
        public Form14()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {// borton aceptar de cambiar idioma
            if (textBox1.Text == "")
            {
                MessageBox.Show("Debe de proporcionar la clave actual.");
            }
            else
            {
                if (comboBox1.SelectedIndex == -1)
                {
                    MessageBox.Show("Debes de seleccionar el idioma");
                }
                else
                {
                    string connectionString = "datasource=localhost;port=3307;username=root;password=1234;database=ensambladora;";
                    string query = "update Usuarios set idioma='" + (comboBox1.SelectedIndex + 1).ToString() + "' where cuenta='" + Form1.cuenta
                        + "' and clave=md5('" + textBox1.Text + "')";
                    MySqlConnection databaseConnection = new MySqlConnection(connectionString);
                    MySqlCommand commandDatabase = new MySqlCommand(query, databaseConnection);
                    int reader;
                    try
                    {
                        databaseConnection.Open();
                        reader = commandDatabase.ExecuteNonQuery();
                        if (reader!=0)
                        {
                            MessageBox.Show("Se modifico el idioma exitosamente.");
                            Close();
                        }
                        else
                        {
                            MessageBox.Show("La contraseña no es correcta.");
                        }
                        
                    }
                    catch (Exception)
                    {
                        MessageBox.Show("Error al modificar el idioma");
                    }
                }
            }

        }

        private void Form14_Load(object sender, EventArgs e)
        {//Load del form cambiar idioma
            comboBox1.Items.Add("Español");
            comboBox1.Items.Add("Ingles");

            if (Form1.idioma == "1") comboBox1.SelectedIndex = 0;
            else comboBox1.SelectedIndex = 1;
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }
    }
}
