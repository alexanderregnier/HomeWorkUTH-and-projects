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
    public partial class Form11 : Form
    {
        public Form11()
        {
            InitializeComponent();
        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {//Boton buscar del form usuarios
            string connectionString = "datasource=localhost;port=3307;username=root;password=1234;database=ensambladora;";
            string query = "Select * from usuarios";
            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query, databaseConnection);
            MySqlDataReader reader;
            dataGridView1.Rows.Clear();
            try
            {
                databaseConnection.Open();
                reader = commandDatabase.ExecuteReader();
                if (reader.HasRows)
                {
                    while (reader.Read())
                    {
                        dataGridView1.Rows.Add(reader.GetString(0), reader.GetString(1), reader.GetString(2),
                        reader.GetString(3), reader.GetString(4), reader.GetString(5));//((reader.GetString(5) == "1") ? "Español" : "Ingles")
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
        }

        private void button2_Click(object sender, EventArgs e)
        {//Boton Agregar del form Usuarios 
            string connectionString = "datasource=localhost;port=3307;username=root;password=1234;database=ensambladora;";
            string query = "insert into usuarios values(null,'" + textBox3.Text + "','" + textBox4.Text + "', md5('"
            + textBox4.Text + "'),'" + (comboBox1.SelectedIndex + 1).ToString() + "','" + (comboBox2.SelectedIndex + 1).ToString() + "')";
            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query, databaseConnection);
            MySqlDataReader reader;
            databaseConnection.Open();
            reader = commandDatabase.ExecuteReader();
            databaseConnection.Close();
            button1_Click(sender, e); //Buscar
        }

        private void Form11_Load(object sender, EventArgs e)
        {//load form usuarios
            if (Form1.idioma == "2")
            {
                this.Text = "Sales";
                button1.Text = "Search";
                button2.Text = "Add";
                button3.Text = "Delete";
                button4.Text = "Update";
                button5.Text = "Exit";
            }
            comboBox1.Items.Add("Administrador");
            comboBox1.Items.Add("Operador");

            comboBox2.Items.Add("Español");
            comboBox2.Items.Add("Ingles");
        }

        private void button3_Click(object sender, EventArgs e)
        {//Boton Eliminar del form usuarios
            string connectionString = "datasource=localhost;port=3307;username=root;password=1234;database=ensambladora;";
            string query = "delete from usuarios where Id_usuario=" + textBox2.Text;
            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query, databaseConnection);
            MySqlDataReader reader;
            databaseConnection.Open();
            reader = commandDatabase.ExecuteReader();
            databaseConnection.Close();
            button1_Click(sender, e); //Buscar
        }

        private void button4_Click(object sender, EventArgs e)
        {//boton modificar del form usuarios
            string connectionString = "datasource=localhost;port=3307;username=root;password=1234;database=ensambladora;";
            string query = "update usuarios set Usuario='"
            + textBox3.Text + "', Cuenta='"
            + textBox4.Text + "', nivel='"
            + (comboBox1.SelectedIndex + 1).ToString() + "', Idioma='"
            + (comboBox2.SelectedIndex + 1).ToString() + "' where Id_usuario=" + textBox2.Text;
            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query, databaseConnection);
            MySqlDataReader reader;
            try
            {
                databaseConnection.Open();
                reader = commandDatabase.ExecuteReader();
                databaseConnection.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            button1_Click(sender, e); //Buscar
        }
        private void textBox2_Leave(object sender, EventArgs e)
        {//leave del textbox2
            Int64 n;
            if (textBox2.Text != "")
            {
                try
                {
                    n = Convert.ToInt64(textBox2.Text);
                }
                catch (Exception xx)
                {
                    MessageBox.Show("El formato no es correcto.\nAcepta solo digitos\n" + xx.Message);
                    textBox2.Focus();
                }
            }
        }

        private void textBox3_Leave(object sender, EventArgs e)
        {//leave del textbox3
            String n;
            if (textBox3.Text != "")
            {
                try
                {
                    n = Convert.ToString(textBox3.Text);
                }
                catch (Exception xx)
                {
                    MessageBox.Show("El formato no es correcto.\nAcepta solo digitos\n" + xx.Message);
                    textBox3.Focus();
                }
            }
        }

        private void textBox4_Leave(object sender, EventArgs e)
        {//leave del textbox 4
            String n;
            if (textBox4.Text != "")
            {
                try
                {
                    n = Convert.ToString(textBox4.Text);
                }
                catch (Exception xx)
                {
                    MessageBox.Show("El formato no es correcto.\nAcepta solo digitos\n" + xx.Message);
                    textBox4.Focus();
                }
            }
        }

        private void textBox5_Leave(object sender, EventArgs e)
        {
     
        }

        private void textBox6_Leave(object sender, EventArgs e)
        {
            
        }

        private void textBox7_Leave(object sender, EventArgs e)
        {
           
        }

        private void dataGridView1_CellClick_1(object sender, DataGridViewCellEventArgs e)
        {//cellclick del datagrid
            if (e.RowIndex != -1)
            {
                textBox2.Text = dataGridView1.Rows[e.RowIndex].Cells[0].Value.ToString();
                textBox3.Text = dataGridView1.Rows[e.RowIndex].Cells[1].Value.ToString();
                textBox4.Text = dataGridView1.Rows[e.RowIndex].Cells[2].Value.ToString();
                if (dataGridView1.Rows[e.RowIndex].Cells[4].Value.ToString() == "1")
                    comboBox1.SelectedIndex = 0;
                else
                    comboBox1.SelectedIndex = 1;

                if (dataGridView1.Rows[e.RowIndex].Cells[5].Value.ToString() == "1")
                    comboBox2.SelectedIndex = 0;
                else
                    comboBox2.SelectedIndex = 1;
                
            }
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void comboBox2_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}
