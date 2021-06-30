template<class type>
class heap {
	private:
		int n = 0;
		struct node {
			type key;
			node *l, *r, *p, *bfr, *afr;
		};
		node *root = NULL, *last = NULL, *lastparent = NULL;
		void free(node *v) {
			if(v) {
				free(v->l);
				free(v->r);
				delete v;
			}
		}
	public:
		void push(type key) {
			if(n == 0) {
				root = new node{key,NULL,NULL,NULL,NULL,NULL};
				last = root;
				lastparent = root;
			} else {
				node *v = new node{key,NULL,NULL,NULL,last,NULL};
				last->afr = v;
				last = v;
				if(lastparent->r) {
					lastparent = lastparent->afr;
					lastparent->l = v;
				} else if(lastparent->l)
					lastparent->r = v;
				else
					lastparent->l = v;
				v->p = lastparent;
				while(v->p) {
					if(v->key < v->p->key)
						swap(v->key,v->p->key);
					else
						break;
					v = v->p;
				}
			}
			n++;
		}
		void pop() {
			if(n == 1) {
				delete root;
				root = NULL;
				last = NULL;
				lastparent = NULL;
				n--;
			} else if(n) {
				node *temp = last, *s;
				if(lastparent->r)
					lastparent->r = NULL;
				else {
					lastparent->l = NULL;
					if(n > 3)
						lastparent = lastparent->bfr;
				}
				root->key = temp->key;
				last = last->bfr;
				last->afr = NULL;
				delete temp;
				temp = root;
				while(temp->l) {
					s = temp->l;
					if(temp->r)
						if(temp->r->key < s->key)
							s = temp->r;
					if(s->key < temp->key)
						swap(s->key,temp->key);
					else
						break;
					temp = s;
				}
				n--;			
			}
		}
		type top() {
			if(root)
				return root->key;
		}
		int size() {
			return n;
		}
		bool empty() {
			return n == 0;
		}
		~heap() {
			free(root);
		}
};
