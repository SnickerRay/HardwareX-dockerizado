
import { StatusBar } from 'expo-status-bar';
import {
  Alert,
  FlatList,
  Image,
  Keyboard,
  KeyboardAvoidingView,
  Platform,
  Pressable,
  StyleSheet,
  Text,
  TextInput,
  TouchableWithoutFeedback,
  View,
} from 'react-native';
import { useCallback, useMemo, useState } from 'react';

type Product = {
  id: string;
  name: string;
  category: string;
  description: string;
  price: number;
  image: string;
};

type Contact = {
  id: string;
  name: string;
  phone: string;
};

const PRODUCTS: Product[] = [
  {
    id: '1',
    name: 'Café Latte',
    category: 'Café con leche',
    description: 'Espresso suave con leche cremosa.',
    price: 8500,
    image: 'https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=800',
  },
  {
    id: '2',
    name: 'Capuchino',
    category: 'Café con leche',
    description: 'Espresso con leche espumosa y cacao.',
    price: 9000,
    image: 'https://images.unsplash.com/photo-1517701604599-bb29b565090c?w=800',
  },
  {
    id: '3',
    name: 'Café Americano',
    category: 'Café negro',
    description: 'Café intenso y aromático.',
    price: 6500,
    image: 'https://images.unsplash.com/photo-1511920170033-f8396924c348?w=800',
  },
  {
    id: '4',
    name: 'Espresso',
    category: 'Café negro',
    description: 'Un café corto, concentrado y fuerte.',
    price: 5000,
    image: 'https://images.unsplash.com/photo-1510707577719-ae7c14805e76?w=800',
  },
  {
    id: '5',
    name: 'Mocaccino',
    category: 'Café con chocolate',
    description: 'Café, leche y un toque de chocolate.',
    price: 9500,
    image: 'https://images.unsplash.com/photo-1570968915860-54d5c301fa9f?w=800',
  },
  {
    id: '6',
    name: 'Chocolate Caliente',
    category: 'Chocolate',
    description: 'Chocolate caliente, dulce y cremoso.',
    price: 8000,
    image: 'https://images.unsplash.com/photo-1542990253-0b8be8a7f9b8?w=800',
  },
  {
    id: '7',
    name: 'Café Helado',
    category: 'Bebida fría',
    description: 'Café refrescante servido con hielo.',
    price: 10000,
    image: 'https://images.unsplash.com/photo-1517701604599-bb29b565090c?w=800',
  },
  {
    id: '8',
    name: 'Frappé de Café',
    category: 'Bebida fría',
    description: 'Café frío mezclado con hielo y leche.',
    price: 12000,
    image: 'https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=800',
  },
  {
    id: '9',
    name: 'Té Chai',
    category: 'Té',
    description: 'Té especiado con un toque de leche.',
    price: 7500,
    image: 'https://images.unsplash.com/photo-1544787219-7f47ccb76574?w=800',
  },
  {
    id: '10',
    name: 'Té Verde',
    category: 'Té',
    description: 'Una bebida suave y aromática.',
    price: 6000,
    image: 'https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=800',
  },
  {
    id: '11',
    name: 'Latte de Vainilla',
    category: 'Café con leche',
    description: 'Latte cremoso con esencia de vainilla.',
    price: 10000,
    image: 'https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=800',
  },
  {
    id: '12',
    name: 'Latte de Caramelo',
    category: 'Café con leche',
    description: 'Espresso con leche y dulce caramelo.',
    price: 10500,
    image: 'https://images.unsplash.com/photo-1517701604599-bb29b565090c?w=800',
  },
];

const CONTACTS: Contact[] = [
  { id: '1', name: 'Ana García', phone: '3001234567' },
  { id: '2', name: 'Carlos Rodríguez', phone: '3102345678' },
  { id: '3', name: 'María López', phone: '3203456789' },
  { id: '4', name: 'Juan Martínez', phone: '3014567890' },
  { id: '5', name: 'Laura Torres', phone: '3155678901' },
  { id: '6', name: 'Andrés Gómez', phone: '3006789012' },
  { id: '7', name: 'Sofía Ramírez', phone: '3117890123' },
  { id: '8', name: 'Daniel Pérez', phone: '3218901234' },
  { id: '9', name: 'Valentina Díaz', phone: '3029012345' },
  { id: '10', name: 'Mateo Sánchez', phone: '3160123456' },
  { id: '11', name: 'Camila Herrera', phone: '3001122334' },
  { id: '12', name: 'Sebastián Castro', phone: '3102233445' },
];

export default function App() {
  const [isRefreshing, setIsRefreshing] = useState(false);

  const [query, setQuery] = useState<string>('');

  const [activeScreen, setActiveScreen] = useState<'products' | 'contacts'>('products');

  const handleRefresh = useCallback(async () => {
    setIsRefreshing(true);

    await new Promise<void>((resolve) => {
      setTimeout(resolve, 1200);
    });

    setIsRefreshing(false);
  }, []);

  const renderProduct = useCallback(
    ({ item }: { item: Product }) => (
      <Pressable
        style={({ pressed }) => [
          styles.card,
          pressed && styles.itemPressed,
        ]}
        onPress={() => {
          Alert.alert(
            'Producto seleccionado',
            `${item.name}\nPrecio: ${formatPrice(item.price)}`
          );
        }}
      >
        <Image
          source={{ uri: item.image }}
          style={styles.productImage}
        />

        <View style={styles.productInfo}>
          <Text style={styles.productName}>{item.name}</Text>

          <Text style={styles.productCategory}>
            {item.category}
          </Text>

          <Text style={styles.productDescription}>
            {item.description}
          </Text>

          <Text style={styles.price}>
            {formatPrice(item.price)}
          </Text>

          <View style={styles.button}>
            <Text style={styles.buttonText}>Ver producto</Text>
          </View>
        </View>
      </Pressable>
    ),
    []
  );

  const filteredContacts = useMemo(() => {
    const lower = query.trim().toLowerCase();

    if (!lower) {
      return CONTACTS;
    }

    return CONTACTS.filter(
      (contact) =>
        contact.name.toLowerCase().includes(lower) ||
        contact.phone.includes(lower)
    );
  }, [query]);

  const renderContact = useCallback(
    ({ item }: { item: Contact }) => (
      <Pressable
        style={({ pressed }) => [
          styles.contactCard,
          pressed && styles.itemPressed,
        ]}
        onPress={() => {
          Keyboard.dismiss();

          Alert.alert(
            'Contacto seleccionado',
            `${item.name}\nTeléfono: ${item.phone}`
          );
        }}
      >
        <View style={styles.avatar}>
          <Text style={styles.avatarText}>
            {item.name.charAt(0)}
          </Text>
        </View>

        <View style={styles.contactInfo}>
          <Text style={styles.contactName}>{item.name}</Text>
          <Text style={styles.contactPhone}>{item.phone}</Text>
        </View>
      </Pressable>
    ),
    []
  );

  const renderEmptyContacts = () => (
    <View style={styles.emptyContainer}>
      <Text style={styles.emptyText}>
        Sin resultados para &quot;{query}&quot;
      </Text>

      <Text style={styles.emptySubText}>
        Intenta con otro nombre o número.
      </Text>
    </View>
  );

  return (
   <KeyboardAvoidingView
    style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
    >
      <TouchableWithoutFeedback onPress={Keyboard.dismiss}>
        <View style={styles.inner}>
          <StatusBar style="dark" />

          <View style={styles.header}>
            <Text style={styles.title}>CAFÉ DE LA CASA</Text>

            <Text style={styles.subtitle}>
              Un buen café cambia tu día.
            </Text>
          </View>

          <View style={styles.tabs}>
            <Pressable
              style={[
                styles.tab,
                activeScreen === 'products' && styles.activeTab,
              ]}
              onPress={() => {
                Keyboard.dismiss();
                setActiveScreen('products');
              }}
            >
              <Text
                style={[
                  styles.tabText,
                  activeScreen === 'products' && styles.activeTabText,
                ]}
              >
                Catálogo
              </Text>
            </Pressable>

            <Pressable
              style={[
                styles.tab,
                activeScreen === 'contacts' && styles.activeTab,
              ]}
              onPress={() => setActiveScreen('contacts')}
            >
              <Text
                style={[
                  styles.tabText,
                  activeScreen === 'contacts' && styles.activeTabText,
                ]}
              >
                Contactos
              </Text>
            </Pressable>
          </View>

          {activeScreen === 'products' ? (
            <FlatList
              style={styles.list}
              contentContainerStyle={styles.listContent}
              data={PRODUCTS}
              keyExtractor={(item) => item.id}
              renderItem={renderProduct}
              ItemSeparatorComponent={() => (
                <View style={styles.separator} />
              )}
              ListHeaderComponent={
                <Text style={styles.listHeader}>
                  Catálogo de Productos
                </Text>
              }
              ListEmptyComponent={
                <Text style={styles.emptyText}>
                  No hay productos disponibles.
                </Text>
              }
              refreshing={isRefreshing}
              onRefresh={handleRefresh}
              showsVerticalScrollIndicator={false}
            />
          ) : (
            <View style={styles.contactsSection}>
              <Text style={styles.listHeader}>
                Buscar contactos
              </Text>

              <TextInput
                style={styles.searchInput}
                placeholder="Buscar contacto..."
                placeholderTextColor="#8b949e"
                value={query}
                onChangeText={setQuery}
                keyboardType="default"
                returnKeyType="search"
                clearButtonMode="while-editing"
              />

              <Text style={styles.resultsText}>
                {filteredContacts.length}{' '}
                {filteredContacts.length === 1
                  ? 'contacto encontrado'
                  : 'contactos encontrados'}
              </Text>

              <FlatList
                style={styles.list}
                contentContainerStyle={styles.listContent}
                data={filteredContacts}
                keyExtractor={(item) => item.id}
                renderItem={renderContact}
                ItemSeparatorComponent={() => (
                  <View style={styles.separator} />
                )}
                ListEmptyComponent={renderEmptyContacts}
                keyboardShouldPersistTaps="handled"
                showsVerticalScrollIndicator={false}
              />
            </View>
          )}
        </View>
      </TouchableWithoutFeedback>
    </KeyboardAvoidingView>
  );
}

function formatPrice(price: number): string {
  return `$ ${price.toLocaleString('es-CO')}`;
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5EBDD',
  },

  inner: {
    flex: 1,
  },

  header: {
    alignItems: 'center',
    paddingTop: 18,
    paddingBottom: 16,
    paddingHorizontal: 16,
  },

  title: {
    fontSize: 27,
    fontWeight: 'bold',
    color: '#4B2E24',
    textAlign: 'center',
  },

  subtitle: {
    fontSize: 15,
    color: '#795548',
    marginTop: 6,
    textAlign: 'center',
  },

  tabs: {
    flexDirection: 'row',
    marginHorizontal: 16,
    marginBottom: 8,
    backgroundColor: '#E8D8C3',
    borderRadius: 12,
    padding: 4,
  },

  tab: {
    flex: 1,
    alignItems: 'center',
    paddingVertical: 11,
    borderRadius: 9,
  },

  activeTab: {
    backgroundColor: '#4B2E24',
  },

  tabText: {
    color: '#4B2E24',
    fontSize: 15,
    fontWeight: '600',
  },

  activeTabText: {
    color: '#FFFFFF',
  },

  list: {
    flex: 1,
  },

  listContent: {
    paddingHorizontal: 16,
    paddingTop: 8,
    paddingBottom: 28,
    flexGrow: 1,
  },

  listHeader: {
    fontSize: 21,
    fontWeight: 'bold',
    color: '#4B2E24',
    marginBottom: 16,
  },

  card: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    padding: 12,
    borderRadius: 16,
    gap: 12,
  },

  productImage: {
    width: 105,
    height: 125,
    borderRadius: 12,
    backgroundColor: '#E8D8C3',
  },

  productInfo: {
    flex: 1,
  },

  productName: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#4B2E24',
  },

  productCategory: {
    fontSize: 12,
    color: '#B77945',
    marginTop: 4,
    fontWeight: '600',
  },

  productDescription: {
    fontSize: 12,
    color: '#795548',
    marginTop: 5,
    lineHeight: 17,
  },

  price: {
    fontSize: 17,
    fontWeight: 'bold',
    color: '#B77945',
    marginTop: 8,
  },

  button: {
    backgroundColor: '#4B2E24',
    paddingVertical: 8,
    paddingHorizontal: 10,
    borderRadius: 9,
    alignItems: 'center',
    marginTop: 8,
  },

  buttonText: {
    color: '#FFFFFF',
    fontSize: 12,
    fontWeight: 'bold',
  },

  separator: {
    height: 1,
    backgroundColor: '#D8C5AF',
    marginVertical: 10,
  },

  itemPressed: {
    opacity: 0.65,
  },

  contactsSection: {
    flex: 1,
    paddingHorizontal: 16,
    paddingTop: 8,
  },

  searchInput: {
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: '#D8C5AF',
    borderRadius: 12,
    paddingHorizontal: 14,
    paddingVertical: 12,
    fontSize: 16,
    color: '#4B2E24',
    marginBottom: 12,
  },

  resultsText: {
    color: '#795548',
    fontSize: 13,
    marginBottom: 10,
  },

  contactCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    padding: 14,
    borderRadius: 12,
    gap: 12,
  },

  avatar: {
    width: 46,
    height: 46,
    borderRadius: 23,
    backgroundColor: '#E8D8C3',
    alignItems: 'center',
    justifyContent: 'center',
  },

  avatarText: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#4B2E24',
  },

  contactInfo: {
    flex: 1,
  },

  contactName: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#4B2E24',
  },

  contactPhone: {
    fontSize: 14,
    color: '#795548',
    marginTop: 4,
  },

  emptyContainer: {
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingVertical: 35,
  },

  emptyText: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#4B2E24',
    textAlign: 'center',
  },

  emptySubText: {
    fontSize: 14,
    color: '#795548',
    marginTop: 8,
    textAlign: 'center',
  },
});
