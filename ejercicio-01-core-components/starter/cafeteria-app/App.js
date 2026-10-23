
import { StatusBar } from 'expo-status-bar';
import { Image, ScrollView, StyleSheet, Text, View, Pressable } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <Text style={styles.title}>CAFÉ DE LA CASA</Text>
        <Text style={styles.subtitle}>Un buen café cambia tu día.</Text>

        <View style={styles.card}>
          <Image
            source={{
              uri: 'https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=800',
            }}
            style={styles.productImage}
          />

          <Text style={styles.productName}>Café Latte</Text>

          <Text style={styles.productDescription}>
            Espresso suave con leche cremosa.
          </Text>

          <Text style={styles.price}>$ 8.500</Text>
          
            <Pressable
              style={styles.button}
              onPress={() => alert('¡Café Latte agregado al pedido!')}
            >
              <Text style={styles.buttonText}>Agregar al pedido</Text>
            </Pressable>

        </View>
        
        <View style={styles.card}>
          <Image
            source={{
              uri: 'https://images.unsplash.com/photo-1517701604599-bb29b565090c?w=800',
            }}
            style={styles.productImage}
          />

          <Text style={styles.productName}>Capuchino</Text>

          <Text style={styles.productDescription}>
            Café espresso con leche espumosa y un toque de cacao.
          </Text>

          <Text style={styles.price}>$ 9.000</Text>
          
            <Pressable
              style={styles.button}
              onPress={() => alert('¡Capuchino agregado al pedido!')}
            >
              <Text style={styles.buttonText}>Agregar al pedido</Text>
            </Pressable>

        </View>

        
        <View style={styles.card}>
          <Image
            source={{
              uri: 'https://images.unsplash.com/photo-1511920170033-f8396924c348?w=800',
            }}
            style={styles.productImage}
          />

          <Text style={styles.productName}>Café Americano</Text>

          <Text style={styles.productDescription}>
            Café intenso y aromático, ideal para cualquier momento.
          </Text>

          <Text style={styles.price}>$ 6.500</Text>
          <Pressable style={styles.button}
              onPress={() => alert('¡Café Americano agregado al pedido!')}
            >
              <Text style={styles.buttonText}>Agregar al pedido</Text>
            </Pressable>

        </View>

      </ScrollView>

      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5EBDD',
  },
  scrollContent: {
    alignItems: 'center',
    paddingVertical: 24,
    paddingHorizontal: 16,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#4B2E24',
  },
  subtitle: {
    fontSize: 16,
    color: '#795548',
    marginTop: 10,
  },
  card: {
    backgroundColor: '#FFFFFF',
    width: '100%',
    maxWidth: 340,
    padding: 16,
    borderRadius: 18,
    marginTop: 30,
  },
  productImage: {
    width: '100%',
    height: 180,
    borderRadius: 12,
  },
  productName: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#4B2E24',
    marginTop: 12,
  },
  productDescription: {
    fontSize: 14,
    color: '#795548',
    marginTop: 6,
  },
  price: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#B77945',
    marginTop: 12,
  },
  
  button: {
    backgroundColor: '#4B2E24',
    padding: 14,
    borderRadius: 12,
    alignItems: 'center',
    marginTop: 16,
  },
  buttonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: 'bold',
  },

});
